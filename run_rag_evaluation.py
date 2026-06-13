"""run_rag_evaluation.py — Evaluate RAG system by running 5 queries in with-corpus and without-corpus modes."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

# Setup paths
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import memory
import index_phd_corpus

DEST_DIR = HERE / "sandbox" / "docmind_project"
TRACES_DIR = DEST_DIR / "traces"
TRACES_DIR.mkdir(parents=True, exist_ok=True)

QUERIES = [
    {
        "id": "query_1",
        "type": "Fact Retrieval (Author & Affiliation)",
        "question": "Who authored the APCO research companion guide, and what is their academic department and university?",
    },
    {
        "id": "query_2",
        "type": "Fact Retrieval (System Config)",
        "question": "What specific on-device embedding model is used by the DocuMind mobile application, and how is it integrated?",
    },
    {
        "id": "query_3",
        "type": "Semantic Recall (Formula)",
        "question": "How is the utility score calculated by the policy controller in this research to determine the optimal configuration for chunking and workers?",
    },
    {
        "id": "query_4",
        "type": "Semantic Recall (Mobile Trilemma)",
        "question": "What three competing priorities form the difficult triad in on-device document processing on mobile platforms?",
    },
    {
        "id": "query_5",
        "type": "Semantic Recall (Analogy)",
        "question": "Explain the food preparation analogy used to describe the role of parallel worker allocation and chunking decisions.",
    }
]


def run_agent_query(query: str) -> str:
    """Run the agent7.py script in a subprocess and capture stdout/stderr."""
    print(f"[eval] executing agent query: {query}")
    env = dict(os.environ)
    env["RAG_OFFLINE"] = "1"
    env["MAX_ITERATIONS"] = "5"
    res = subprocess.run(
        ["uv", "run", "agent7.py", query],
        cwd=str(HERE),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
        env=env,
    )
    # Combine stdout and stderr for full trace
    full_output = []
    if res.stdout:
        full_output.append(res.stdout)
    if res.stderr:
        # Filter out common noise from stderr if any
        stderr_clean = "\n".join(
            line for line in res.stderr.splitlines()
            if "INFO" not in line and "Processing request" not in line
        )
        if stderr_clean.strip():
            full_output.append(stderr_clean)
    
    return "\n".join(full_output)


def main() -> None:
    # --- PHASE 1: WITHOUT CORPUS ---
    print("\n" + "=" * 50)
    print("PHASE 1: EVALUATING WITHOUT CORPUS (NO INDEX)")
    print("=" * 50)
    
    # 1. Clear database
    print("[eval] clearing memory database...")
    memory.clear()
    
    no_corpus_traces = {}
    for q in QUERIES:
        qid = q["id"]
        question = q["question"]
        print(f"\n[eval] Running {qid} without index...")
        trace = run_agent_query(question)
        no_corpus_traces[qid] = trace
        time.sleep(5)  # cool down the LLM rate limits

    # --- PHASE 2: INDEXING CORPUS ---
    print("\n" + "=" * 50)
    print("PHASE 2: INDEXING THE DOCMIND PROJECT CORPUS")
    print("=" * 50)
    # Mirror and index documents
    index_phd_corpus.main()

    # --- PHASE 3: WITH CORPUS ---
    print("\n" + "=" * 50)
    print("PHASE 3: EVALUATING WITH CORPUS (INDEX POPULATED)")
    print("=" * 50)
    
    with_corpus_traces = {}
    for q in QUERIES:
        qid = q["id"]
        question = q["question"]
        print(f"\n[eval] Running {qid} with index...")
        trace = run_agent_query(question)
        with_corpus_traces[qid] = trace
        time.sleep(5)  # cool down the LLM rate limits

    # --- PHASE 4: GENERATING COMPARISONS ---
    print("\n" + "=" * 50)
    print("PHASE 4: WRITING TRACE COMPARISONS")
    print("=" * 50)

    TRACES_DIR.mkdir(parents=True, exist_ok=True)

    for q in QUERIES:
        qid = q["id"]
        question = q["question"]
        qtype = q["type"]
        
        no_trace = no_corpus_traces[qid]
        with_trace = with_corpus_traces[qid]
        
        comparison_md = f"""# Query Evaluation: {qid}
**Query Type**: {qtype}
**Question**: {question}

---

## 🛑 State A: Without Corpus (No Index)

```text
{no_trace}
```

---

## ✅ State B: With Corpus (Indexed)

```text
{with_trace}
```
"""
        dest_file = TRACES_DIR / f"{qid}_comparison.md"
        dest_file.write_text(comparison_md, encoding="utf-8")
        print(f"[eval] Wrote comparison trace to: {dest_file}")

    print("\n" + "=" * 50)
    print("Evaluation Complete! Traces written.")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
