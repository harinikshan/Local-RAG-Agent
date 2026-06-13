"""run_base_traces.py — Run and capture traces of the 8 base/core MCP tools."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Setup paths
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mcp_server
import memory

TRACES_FILE = HERE / "sandbox" / "docmind_project" / "base_traces.md"


def main():
    import shutil
    state_dir = HERE / "state"
    backup_dir = HERE / "state_backup"
    
    # Backup state directory
    if state_dir.exists():
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.copytree(state_dir, backup_dir)
        print("Backed up state directory to state_backup")

    print("Running base tools and generating traces...")
    
    # Ensure memory is cleared for indexing/search trace sanity
    memory.clear()
    
    # We will run the 8 base tools in sequence:
    # 1. get_time
    # 2. create_file
    # 3. read_file
    # 4. update_file
    # 5. edit_file
    # 6. list_dir
    # 7. index_document
    # 8. search_knowledge

    traces = []

    # 1. get_time
    traces.append(run_tool(
        "get_time",
        mcp_server.get_time,
        {"timezone": "Asia/Kolkata"}
    ))

    # 2. create_file
    traces.append(run_tool(
        "create_file",
        mcp_server.create_file,
        {"path": "trace_test.txt", "content": "Initial content for base trace tests."}
    ))

    # 3. read_file
    traces.append(run_tool(
        "read_file",
        mcp_server.read_file,
        {"path": "trace_test.txt"}
    ))

    # 4. update_file
    traces.append(run_tool(
        "update_file",
        mcp_server.update_file,
        {"path": "trace_test.txt", "content": "Updated content for base trace tests. Word1 Word2."}
    ))

    # 5. edit_file
    traces.append(run_tool(
        "edit_file",
        mcp_server.edit_file,
        {"path": "trace_test.txt", "find": "Word1", "replace": "Replacement1"}
    ))

    # 6. list_dir
    traces.append(run_tool(
        "list_dir",
        mcp_server.list_dir,
        {"path": "."}
    ))

    # 7. index_document
    traces.append(run_tool(
        "index_document",
        mcp_server.index_document,
        {"path": "trace_test.txt", "chunk_size": 10, "overlap": 2}
    ))

    # 8. search_knowledge
    traces.append(run_tool(
        "search_knowledge",
        mcp_server.search_knowledge,
        {"query": "Replacement1", "k": 3}
    ))

    # Clean up test file
    test_file = HERE / "sandbox" / "trace_test.txt"
    if test_file.exists():
        test_file.unlink()

    # Compile the final markdown
    md_content = ["# MCP Base Traces\n\nThis file contains the execution traces for the eight core/base tools in the Session 7 MCP server.\n"]
    for t in traces:
        md_content.append(f"## Tool: `{t['name']}`")
        md_content.append(f"**Arguments**:\n```json\n{json.dumps(t['args'], indent=2)}\n```\n")
        md_content.append(f"**Result**:\n```json\n{json.dumps(t['result'], indent=2)}\n```\n")
        md_content.append("---\n")

    TRACES_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACES_FILE.write_text("\n".join(md_content), encoding="utf-8")
    print(f"Base traces written to: {TRACES_FILE}")

    # Restore state directory
    if backup_dir.exists():
        if state_dir.exists():
            shutil.rmtree(state_dir)
        shutil.copytree(backup_dir, state_dir)
        shutil.rmtree(backup_dir)
        print("Restored state directory from state_backup")


def run_tool(name: str, fn, args: dict) -> dict:
    print(f"  Running `{name}`...")
    try:
        res = fn(**args)
        return {"name": name, "args": args, "result": res}
    except Exception as e:
        return {"name": name, "args": args, "result": {"error": str(e)}}


if __name__ == "__main__":
    main()
