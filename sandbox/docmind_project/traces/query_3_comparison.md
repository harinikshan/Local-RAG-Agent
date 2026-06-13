# Query Evaluation: query_3
**Query Type**: Semantic Recall (Formula)
**Question**: How is the utility score calculated by the policy controller in this research to determine the optimal configuration for chunking and workers?

---

## 🛑 State A: Without Corpus (No Index)

```text

══════════════════════════════════════════════════════════════════════════════
run 8424437f  ─  query: How is the utility score calculated by the policy controller in this research to determine the optimal configuration for chunking and workers?
══════════════════════════════════════════════════════════════════════════════
[mcp] loaded 11 tools: ['web_search', 'fetch_url', 'get_time', 'currency_convert', 'read_file', 'list_dir', 'create_file', 'update_file', 'edit_file', 'index_document', 'search_knowledge']

─── iter 1 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ○ g:d397e910 — Query the existing knowledge base
[perception]    ○ g:431e43d4 — Answer the question about utility score calculation
[decision]      TOOL_CALL: search_knowledge({"query": "utility score calculation by policy controller for chunking and workers configuration", "k": 5})
[action]        → {   "id": "mem:4fae7e8a",   "descriptor": "Policy controller calculates utility score for chunking and workers configuration",   "source": "user_query",   "chunk": "",   "metadata": {     "entities": ...

─── iter 2 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ✓ g:d397e910 — Query the existing knowledge base
[perception]    ○ g:431e43d4 — Answer the question about utility score calculation
[decision] loop detected for search_knowledge({"query": "utility score calculation by policy controller fo) — forcing synthesis
[decision]      ANSWER: The utility score calculation by the policy controller for chunking and workers configuration is determined to find the optimal configuration. The policy controller calculates the utility score to ach...

─── iter 3 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ✓ g:d397e910 — Query the existing knowledge base
[perception]    ✓ g:431e43d4 — Answer the question about utility score calculation

[done] all 2 goals satisfied

══════════════════════════════════════════════════════════════════════════════
FINAL: The utility score calculation by the policy controller for chunking and workers configuration is determined to find the optimal configuration. The policy controller calculates the utility score to achieve this goal. Unfortunately, the exact formula or method used for this calculation is not provided in the given memory hits. However, it is clear that the policy controller plays a crucial role in determining the optimal configuration by calculating the utility score for different chunking and workers configurations. 

The memory hits suggest that the policy controller's calculation of the utility score is an important aspect of the research, but the specific details of the calculation are not provided. The hits also mention other topics such as the APCO research companion guide authors and their academic department and university, as well as the DocuMind mobile application's on-device embedding model, but these are not directly related to the utility score calculation.

In summary, while the memory hits provide some context and background information on the topic, they do not provide a clear and direct answer to the question of how the utility score is calculated by the policy controller. The calculation of the utility score is a critical aspect of the policy controller's function, but the exact method or formula used is not specified in the given information.
══════════════════════════════════════════════════════════════════════════════


                             ListToolsRequest                                   
                             CallToolRequest                                    
                             http://localhost:8107/v1/routers                   
                             "HTTP/1.1 200 OK"                                  
                             http://localhost:8107/v1/embed                     
                             "HTTP/1.1 200 OK"                                  
```

---

## ✅ State B: With Corpus (Indexed)

```text

══════════════════════════════════════════════════════════════════════════════
run 09d742d0  ─  query: How is the utility score calculated by the policy controller in this research to determine the optimal configuration for chunking and workers?
══════════════════════════════════════════════════════════════════════════════
[mcp] loaded 11 tools: ['web_search', 'fetch_url', 'get_time', 'currency_convert', 'read_file', 'list_dir', 'create_file', 'update_file', 'edit_file', 'index_document', 'search_knowledge']

─── iter 1 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ○ g:b33d4045 — Query the existing knowledge base about the utility score calculation by the policy controller
[perception]    ○ g:97eabff9 — Summarise the answer to the user's question about the optimal configuration for chunking and workers
[decision]      TOOL_CALL: search_knowledge({"query": "utility score calculation by the policy controller", "k": "5"})
[action]        → [artifact art:b983270549ed914e, 13307 bytes] preview: {   "id": "mem:8ebfbf64",   "descriptor": "Policy controller calculates utility score for optimal chunking and workers configuration",   "source":...   +art:b983270549ed914e

─── iter 2 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ✓ g:b33d4045 — Query the existing knowledge base about the utility score calculation by the policy controller
[perception]    ○ g:97eabff9 — Summarise the answer to the user's question about the optimal configuration for chunking and workers  attach=art:b983270549ed914e
[attach]        art:b983270549ed914e (13307 bytes)
[decision]      TOOL_CALL: search_knowledge({"query": "optimal configuration for chunking and workers", "k": "5"})
[action]        → [artifact art:9fce57c261dc58d1, 13022 bytes] preview: {   "id": "mem:4d196821",   "descriptor": "[sandbox:docmind_project/APCO_PhD_Companion_Guide.pdf chunk 4/13] Chunking is deciding how to divide th...   +art:9fce57c261dc58d1

─── iter 3 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ✓ g:b33d4045 — Query the existing knowledge base about the utility score calculation by the policy controller
[perception]    ○ g:97eabff9 — Summarise the answer to the user's question about the optimal configuration for chunking and workers  attach=art:b983270549ed914e
[attach]        art:b983270549ed914e (13307 bytes)
[decision] loop detected for search_knowledge({"query": "optimal configuration for chunking and workers", ) — forcing synthesis
[decision]      ANSWER: The optimal configuration for chunking and workers is determined by the Adaptive Policy-Controlled Chunking Optimization (APCO) controller, which calculates a utility score based on the quality of the...

─── iter 4 ─────────────────────────────────────────────
[memory.read]   8 hits
[perception]    ✓ g:b33d4045 — Query the existing knowledge base about the utility score calculation by the policy controller
[perception]    ✓ g:97eabff9 — Summarise the answer to the user's question about the optimal configuration for chunking and workers

[done] all 2 goals satisfied

══════════════════════════════════════════════════════════════════════════════
FINAL: The optimal configuration for chunking and workers is determined by the Adaptive Policy-Controlled Chunking Optimization (APCO) controller, which calculates a utility score based on the quality of the decision. The utility score is computed using the formula U = alpha * Q - beta * L - gamma * R, where alpha, beta, and gamma are weights that prioritize retrieval quality, latency, and resource usage, respectively. The APCO controller follows a decision tree to determine the chunking mode and worker count, considering factors such as document character count, density ratio, and device tier.

The decision tree is as follows:

* IF doc_chars < parallel_bypass_threshold (default 20,000): → Use Fixed chunking with 1 worker (small doc bypass)
* ELSE IF density_ratio >= density_threshold (default 0.35): → Use Adaptive chunking
* ELSE: → Use Fixed chunking
* Worker count = clamp(calculated_workers, 1, device_tier_max)

The APCO controller also computes a utility score to measure the quality of the decision, which is based on the quality, latency, and resource scores. The quality score is computed from chunk size relative to optimal range (280-900 chars) and overlap ratio, while the latency score is estimated from document size divided by chunk throughput and worker count. The resource score is based on worker count relative to device tier capacity and estimated memory pressure.

The optimal configuration for chunking and workers is determined by the APCO controller's decision, which balances the trade-offs between retrieval quality, latency, and resource usage. The controller's decision is influenced by the document characteristics, device capabilities, and the weights assigned to the different factors in the utility score calculation. 

In terms of specific numbers, the optimal chunk size is between 280-900 characters, and the optimal worker count is determined by the device tier and the calculated workers. The APCO controller's decision is also influenced by the density ratio of the document, with adaptive chunking being used when the density ratio is above a certain threshold. 

Overall, the APCO controller's decision is based on a complex interplay of factors, and the optimal configuration for chunking and workers will depend on the specific use case and requirements. However, by using the APCO controller's decision tree and utility score calculation, it is possible to determine the optimal configuration for a given scenario. 

The APCO controller's overhead is also an important consideration, as it can range from ~4% to ~17% depending on the workload size and device tier. However, this overhead is amortized over more chunks for larger documents, making the APCO controller a efficient solution for on-device PDF retrieval-augmented generation. 

In conclusion, the optimal configuration for chunking and workers is determined by the APCO controller's decision, which balances the trade-offs between retrieval quality, latency, and resource usage. The controller's decision is influenced by a complex interplay of factors, including document characteristics, device capabilities, and weights assigned to different factors in the utility score calculation. By using the APCO controller's decision tree and utility score calculation, it is possible to determine the optimal configuration for a given scenario, and the controller's overhead is an important consideration in evaluating its efficiency.
══════════════════════════════════════════════════════════════════════════════


                             ListToolsRequest                                   
                             CallToolRequest                                    
                             http://localhost:8107/v1/routers                   
                             "HTTP/1.1 200 OK"                                  
                             http://localhost:8107/v1/embed                     
                             "HTTP/1.1 200 OK"                                  
                             CallToolRequest                                    
                             http://localhost:8107/v1/routers                   
                             "HTTP/1.1 200 OK"                                  
                             http://localhost:8107/v1/embed                     
                             "HTTP/1.1 200 OK"                                  
```
