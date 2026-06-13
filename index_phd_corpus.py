"""index_phd_corpus.py — Mirror and index docmind_project corpus into S7 vector store."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

# Insert current directory into path for local imports
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import memory
import mcp_server

SOURCE_DIR = Path("/Users/cloudtrade/Documents/docmind_project")
SANDBOX_DIR = HERE / "sandbox"
DEST_DIR = SANDBOX_DIR / "docmind_project"


def mirror_corpus() -> list[Path]:
    """Copy all .pdf and .md files from SOURCE_DIR to DEST_DIR, keeping structure."""
    if DEST_DIR.exists():
        shutil.rmtree(DEST_DIR)
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    copied_files: list[Path] = []
    # Walk the directory
    for item in SOURCE_DIR.rglob("*"):
        if item.is_file() and item.suffix.lower() in (".pdf", ".md"):
            # Exclude build, .venv, .git, and hidden directories
            parts = item.relative_to(SOURCE_DIR).parts
            if any(p.startswith(".") or p in ("build", "android", "ios", "macos", "web") for p in parts):
                continue
            
            # Limit corpus to root-level documents (PDF companion guides, user guide, etc.)
            # and the datasets folder (the 45 paper1 PDFs)
            is_root = len(parts) == 1
            is_dataset = "datasets" in parts
            if not (is_root or is_dataset):
                continue
            
            rel_path = item.relative_to(SOURCE_DIR)
            dest_path = DEST_DIR / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_path)
            copied_files.append(dest_path)

    print(f"[mirror] copied {len(copied_files)} documents to sandbox/docmind_project")
    return copied_files


def main() -> None:
    # 1. Clear existing memory index for clean start
    print("[index] clearing old vector index and memory JSON...")
    memory.clear()

    # 2. Mirror files to S7 sandbox
    copied_files = mirror_corpus()

    # 3. Index each file
    indexed_count = 0
    total_chunks = 0
    manifest = []

    for file_path in sorted(copied_files):
        # Path relative to the SANDBOX root directory
        rel_sandbox_path = file_path.relative_to(SANDBOX_DIR)
        rel_str = str(rel_sandbox_path)

        print(f"[index] indexing {rel_str} ...")
        try:
            res = mcp_server.index_document(rel_str)
            chunks_indexed = res.get("chunks_indexed", 0)
            total_chunks += chunks_indexed
            if chunks_indexed > 0:
                indexed_count += 1
                manifest.append({
                    "doc_id": file_path.stem,
                    "rel_path": str(file_path.relative_to(DEST_DIR)),
                    "chunks": chunks_indexed
                })
        except Exception as e:
            print(f"[index] failed to index {rel_str}: {e}")

    # 4. Save manifest of indexed documents
    manifest_path = DEST_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    
    print("\n" + "=" * 50)
    print(f"Indexing Complete!")
    print(f"Indexed documents: {indexed_count}")
    print(f"Total chunks indexed: {total_chunks}")
    print(f"Manifest written to: {manifest_path}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
