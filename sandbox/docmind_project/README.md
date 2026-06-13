# DocuMind PhD Research RAG Application & Evaluation

This repository houses the fully offline Retrieval-Augmented Generation (RAG) system running over the **DocuMind PhD Research Project Corpus**. 

The system leverages:
1.  **FastMCP Stdio Server** containing file tools and vector ingestion (`index_document` and `search_knowledge`).
2.  **pdftotext** CLI backend for local PDF extraction.
3.  **LLM Gateway V7** on port `8107` with automatic provider failover and structured schema validation.
4.  **FAISS Vector Index** backed by local SQLite DB for semantic recall.

---

## 🎥 Video Demo
A video showcase demonstrating the RAG pipeline end-to-end (indexing, querying, comparative evaluation) is available here:
👉 **[Watch the YouTube Demo Video](https://youtu.be/8afUIPWq1ew)**

---

## 📂 Corpus Manifest

The index crawls and ingests a total of **51 files** yielding **211 chunks**. The manifest of all documents is structured below:

| Document ID | Relative Path | Indexed Chunks |
| :--- | :--- | :--- |
| `AGENTS` | `AGENTS.md` | 1 |
| `APCO_BEEI_Complete_Submission_Guide` | `APCO_BEEI_Complete_Submission_Guide.pdf` | 13 |
| `APCO_Complete_Publication_Guide_CORRECTED` | `APCO_Complete_Publication_Guide_CORRECTED.pdf` | 8 |
| `APCO_Journal_Selection_Guide` | `APCO_Journal_Selection_Guide.pdf` | 15 |
| `APCO_Paper_BEEI_Review_Report` | `APCO_Paper_BEEI_Review_Report.pdf` | 8 |
| `APCO_PhD_Companion_Guide` | `APCO_PhD_Companion_Guide.pdf` | 13 |
| `APCO_Telkomnika_Submission_Guide` | `APCO_Telkomnika_Submission_Guide.pdf` | 10 |
| `DocuMind_Application_User_Guide` | `DocuMind_Application_User_Guide.pdf` | 12 |
| `Paper1_Complete_File_Map` | `Paper1_Complete_File_Map.pdf` | 4 |
| `README` | `README.md` | 1 |
| `HRD002` | `datasets/paper1/hard/HRD002.pdf` | 1 |
| `HRD003` | `datasets/paper1/hard/HRD003.pdf` | 1 |
| `HRD004` | `datasets/paper1/hard/HRD004.pdf` | 1 |
| `HRD005` | `datasets/paper1/hard/HRD005.pdf` | 1 |
| `HRD006` | `datasets/paper1/hard/HRD006.pdf` | 5 |
| `HRD007` | `datasets/paper1/hard/HRD007.pdf` | 1 |
| `HRD008` | `datasets/paper1/hard/HRD008.pdf` | 1 |
| `HRD009` | `datasets/paper1/hard/HRD009.pdf` | 1 |
| `HRD010` | `datasets/paper1/hard/HRD010.pdf` | 1 |
| `HRD011` | `datasets/paper1/hard/HRD011.pdf` | 1 |
| `HRD012` | `datasets/paper1/hard/HRD012.pdf` | 1 |
| `HRD013` | `datasets/paper1/hard/HRD013.pdf` | 2 |
| `POL001` | `datasets/paper1/policy/POL001.pdf` | 6 |
| `POL002` | `datasets/paper1/policy/POL002.pdf` | 20 |
| `POL003` | `datasets/paper1/policy/POL003.pdf` | 3 |
| `POL004` | `datasets/paper1/policy/POL004.pdf` | 1 |
| `POL005` | `datasets/paper1/policy/POL005.pdf` | 1 |
| `POL006` | `datasets/paper1/policy/POL006.pdf` | 1 |
| `POL007` | `datasets/paper1/policy/POL007.pdf` | 1 |
| `POL008` | `datasets/paper1/policy/POL008.pdf` | 1 |
| `POL009` | `datasets/paper1/policy/POL009.pdf` | 1 |
| `POL010` | `datasets/paper1/policy/POL010.pdf` | 1 |
| `POL011` | `datasets/paper1/policy/POL011.pdf` | 1 |
| `POL012` | `datasets/paper1/policy/POL012.pdf` | 2 |
| `POL013` | `datasets/paper1/policy/POL013.pdf` | 8 |
| `POL014` | `datasets/paper1/policy/POL014.pdf` | 6 |
| `POL015` | `datasets/paper1/policy/POL015.pdf` | 6 |
| `TEC001` | `datasets/paper1/technical/TEC001.pdf` | 18 |
| `TEC002` | `datasets/paper1/technical/TEC002.pdf` | 3 |
| `TEC003` | `datasets/paper1/technical/TEC003.pdf` | 3 |
| `TEC004` | `datasets/paper1/technical/TEC004.pdf` | 2 |
| `TEC005` | `datasets/paper1/technical/TEC005.pdf` | 1 |
| `TEC007` | `datasets/paper1/technical/TEC007.pdf` | 3 |
| `TEC008` | `datasets/paper1/technical/TEC008.pdf` | 2 |
| `TEC009` | `datasets/paper1/technical/TEC009.pdf` | 5 |
| `TEC010` | `datasets/paper1/technical/TEC010.pdf` | 2 |
| `TEC011` | `datasets/paper1/technical/TEC011.pdf` | 3 |
| `TEC012` | `datasets/paper1/technical/TEC012.pdf` | 3 |
| `TEC013` | `datasets/paper1/technical/TEC013.pdf` | 2 |
| `TEC014` | `datasets/paper1/technical/TEC014.pdf` | 2 |
| `TEC015` | `datasets/paper1/technical/TEC015.pdf` | 1 |

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


---

## 📊 MCP Base Traces
Below are the raw stdout traces of the eight core/base tools generated programmatically by `run_base_traces.py`:

# MCP Base Traces

This file contains the execution traces for the eight core/base tools in the Session 7 MCP server.

## Tool: `get_time`
**Arguments**:
```json
{
  "timezone": "Asia/Kolkata"
}
```

**Result**:
```json
{
  "iso": "2026-06-13T21:36:29.559685+05:30",
  "human": "Saturday, 13 June 2026 21:36:29 IST",
  "timezone": "Asia/Kolkata",
  "offset_hours": 5.5
}
```

---

## Tool: `create_file`
**Arguments**:
```json
{
  "path": "trace_test.txt",
  "content": "Initial content for base trace tests."
}
```

**Result**:
```json
{
  "ok": true,
  "path": "trace_test.txt",
  "size_bytes": 37
}
```

---

## Tool: `read_file`
**Arguments**:
```json
{
  "path": "trace_test.txt"
}
```

**Result**:
```json
{
  "path": "trace_test.txt",
  "size_bytes": 37,
  "content": "Initial content for base trace tests.",
  "encoding": "utf-8"
}
```

---

## Tool: `update_file`
**Arguments**:
```json
{
  "path": "trace_test.txt",
  "content": "Updated content for base trace tests. Word1 Word2."
}
```

**Result**:
```json
{
  "ok": true,
  "path": "trace_test.txt",
  "size_bytes": 50
}
```

---

## Tool: `edit_file`
**Arguments**:
```json
{
  "path": "trace_test.txt",
  "find": "Word1",
  "replace": "Replacement1"
}
```

**Result**:
```json
{
  "ok": true,
  "path": "trace_test.txt",
  "replacements": 1,
  "size_bytes": 57
}
```

---

## Tool: `list_dir`
**Arguments**:
```json
{
  "path": "."
}
```

**Result**:
```json
{
  "path": ".",
  "count": 9,
  "names": [
    "docmind_project",
    "mom_birthday.txt",
    "moms_birthday.txt",
    "papers",
    "reminder_2026-05-01_moms_birthday.txt",
    "reminder_2026-05-15_moms_birthday.txt",
    "reminder_2weeks_before_mom_birthday.txt",
    "reminder_mom_birthday.txt",
    "trace_test.txt"
  ],
  "entries": [
    {
      "name": "docmind_project",
      "type": "dir",
      "size_bytes": 0
    },
    {
      "name": "mom_birthday.txt",
      "type": "file",
      "size_bytes": 33
    },
    {
      "name": "moms_birthday.txt",
      "type": "file",
      "size_bytes": 30
    },
    {
      "name": "papers",
      "type": "dir",
      "size_bytes": 0
    },
    {
      "name": "reminder_2026-05-01_moms_birthday.txt",
      "type": "file",
      "size_bytes": 72
    },
    {
      "name": "reminder_2026-05-15_moms_birthday.txt",
      "type": "file",
      "size_bytes": 91
    },
    {
      "name": "reminder_2weeks_before_mom_birthday.txt",
      "type": "file",
      "size_bytes": 73
    },
    {
      "name": "reminder_mom_birthday.txt",
      "type": "file",
      "size_bytes": 47
    },
    {
      "name": "trace_test.txt",
      "type": "file",
      "size_bytes": 57
    }
  ]
}
```

---

## Tool: `index_document`
**Arguments**:
```json
{
  "path": "trace_test.txt",
  "chunk_size": 10,
  "overlap": 2
}
```

**Result**:
```json
{
  "path": "trace_test.txt",
  "source": "sandbox:trace_test.txt",
  "chunks_indexed": 1,
  "chunk_size": 10,
  "overlap": 2
}
```

---

## Tool: `search_knowledge`
**Arguments**:
```json
{
  "query": "Replacement1",
  "k": 3
}
```

**Result**:
```json
[
  {
    "id": "mem:34c9803d",
    "descriptor": "[sandbox:trace_test.txt chunk 1/1] Updated content for base trace tests. Replacement1 Word2.",
    "source": "sandbox:trace_test.txt",
    "chunk": "Updated content for base trace tests. Replacement1 Word2.",
    "metadata": {
      "chunk_index": 0,
      "total_chunks": 1,
      "source": "sandbox:trace_test.txt"
    }
  },
  {
    "id": "mem:34c9803d",
    "descriptor": "[sandbox:trace_test.txt chunk 1/1] Updated content for base trace tests. Replacement1 Word2.",
    "source": "sandbox:trace_test.txt",
    "chunk": "Updated content for base trace tests. Replacement1 Word2.",
    "metadata": {
      "chunk_index": 0,
      "total_chunks": 1,
      "source": "sandbox:trace_test.txt"
    }
  }
]
```

---

