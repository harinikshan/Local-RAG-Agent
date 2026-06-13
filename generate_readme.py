"""generate_readme.py — Compile final submission README.md with manifest, base traces, and custom traces."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST_PATH = HERE / "sandbox" / "docmind_project" / "manifest.json"
BASE_TRACES_PATH = HERE / "sandbox" / "docmind_project" / "base_traces.md"
README_PATH = HERE / "sandbox" / "docmind_project" / "README.md"


def main():
    print("Generating README.md...")
    
    # 1. Parse manifest
    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found. Run index_phd_corpus.py first.")
        return
    manifest_data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    
    # Generate manifest table
    manifest_rows = []
    total_chunks = 0
    for item in manifest_data:
        doc_id = item["doc_id"]
        rel_path = item["rel_path"]
        chunks = item["chunks"]
        total_chunks += chunks
        manifest_rows.append(f"| `{doc_id}` | `{rel_path}` | {chunks} |")
        
    manifest_table_str = "\n".join(manifest_rows)

    # 2. Read base traces
    if not BASE_TRACES_PATH.exists():
        print(f"Error: {BASE_TRACES_PATH} not found. Run run_base_traces.py first.")
        return
    base_traces_content = BASE_TRACES_PATH.read_text(encoding="utf-8")

    # 3. Custom comparative queries overview
    custom_queries_str = """
Here are the five custom queries designed against the DocuMind PhD corpus. They compare **State A (Without Corpus/Index)** and **State B (With Corpus/Indexed)**.

### Query 1: Fact Retrieval (Author & Affiliation)
*   **Question**: "Who authored the APCO research companion guide, and what is their academic department and university?"
*   **Target Document**: `APCO_PhD_Companion_Guide.pdf`
*   **Comparison Summary**:
    *   **State A (No Index)**: The agent fails to answer because it lacks access to local guides. It performs web searches but finds no correct scientific affiliation.
    *   **State B (Indexed)**: Retrieves the relevant companion guide chunks and identifies **Srisankari** from the **Department of Computer Science** at **Madurai Kamaraj University**.
*   **Trace Detail**: See [query_1_comparison.md](traces/query_1_comparison.md).

### Query 2: Fact Retrieval (System Config)
*   **Question**: "What specific on-device embedding model is used by the DocuMind mobile application, and how is it integrated?"
*   **Target Document**: `DocuMind_Application_User_Guide.pdf`
*   **Comparison Summary**:
    *   **State A (No Index)**: The agent has no knowledge of the custom app's configuration and abstains or fails to locate details online.
    *   **State B (Indexed)**: Correctly retrieves the user guide chunks specifying the **Qwen3 0.6B Embed** model integrated via the **Cactus SDK**.
*   **Trace Detail**: See [query_2_comparison.md](traces/query_2_comparison.md).

### Query 3: Semantic Recall (Formula)
*   **Question**: "How is the utility score calculated by the policy controller in this research to determine the optimal configuration for chunking and workers?"
*   **Target Document**: `datasets/paper1/policy/POL002.pdf`
*   **Comparison Summary**:
    *   **State A (No Index)**: Bypasses the vector database and fails to find any specific mathematical formula or local policy guidelines.
    *   **State B (Indexed)**: Recalls the exact utility score calculation based on the weighted sum of Accuracy, Throughput, and Resource overhead penalties.
*   **Trace Detail**: See [query_3_comparison.md](traces/query_3_comparison.md).

### Query 4: Semantic Recall (Mobile Trilemma)
*   **Question**: "What three competing priorities form the difficult triad in on-device document processing on mobile platforms?"
*   **Target Document**: `datasets/paper1/technical/TEC001.pdf`
*   **Comparison Summary**:
    *   **State A (No Index)**: The agent has no access to the technical paper and gives a generic answer about standard web trilemmas.
    *   **State B (Indexed)**: Recalls the specific "difficult triad" parameters — **Accuracy, Latency, and Power/Memory efficiency** — under strict hardware constraint boundaries.
*   **Trace Detail**: See [query_4_comparison.md](traces/query_4_comparison.md).

### Query 5: Semantic Recall (Analogy)
*   **Question**: "Explain the food preparation analogy used to describe the role of parallel worker allocation and chunking decisions."
*   **Target Document**: `datasets/paper1/technical/TEC009.pdf`
*   **Comparison Summary**:
    *   **State A (No Index)**: Lacks contextual awareness and cannot explain this unique food analogy.
    *   **State B (Indexed)**: Successfully retrieves chunks outlining the analogy, where parallel workers are compared to kitchen chefs, chunk sizes to meal prep stages, and scheduling controls to sous-chef coordination.
*   **Trace Detail**: See [query_5_comparison.md](traces/query_5_comparison.md).
"""

    # Assemble the final README.md content
    readme_content = f"""# DocuMind PhD Research RAG Application & Evaluation

This repository houses the fully offline Retrieval-Augmented Generation (RAG) system running over the **DocuMind PhD Research Project Corpus**. 

The system leverages:
1.  **FastMCP Stdio Server** containing file tools and vector ingestion (`index_document` and `search_knowledge`).
2.  **pdftotext** CLI backend for local PDF extraction.
3.  **LLM Gateway V7** on port `8107` with automatic provider failover and structured schema validation.
4.  **FAISS Vector Index** backed by local SQLite DB for semantic recall.

---

## 🎥 Video Demo
A video showcase demonstrating the RAG pipeline end-to-end (indexing, querying, comparative traces) is submitted alongside this repository.

---

## 📂 Corpus Manifest

The index crawls and ingests a total of **{len(manifest_data)} files** yielding **{total_chunks} chunks**. The manifest of all documents is structured below:

| Document ID | Relative Path | Indexed Chunks |
| :--- | :--- | :--- |
{manifest_table_str}

---

## 🚀 How to Run

1.  **Prerequisites**: Ensure the LLM Gateway V7 is running locally on port `8107`.
2.  **Environment Setup**: Verify that `.env` is configured with valid provider keys.
3.  **Ingestion & Evaluation**:
    ```bash
    # Index the corpus (copies 50+ items to sandbox and populates FAISS/SQLite)
    uv run python index_phd_corpus.py
    
    # Execute the 5-query comparative evaluation suite
    uv run python run_rag_evaluation.py
    ```

---

## 🔍 Five Custom Comparative Traces
{custom_queries_str}

---

## 📊 MCP Base Traces
Below are the raw stdout traces of the eight core/base tools generated programmatically by `run_base_traces.py`:

{base_traces_content}
"""

    README_PATH.write_text(readme_content, encoding="utf-8")
    print(f"Submission README.md successfully compiled at: {README_PATH}")


if __name__ == "__main__":
    main()
