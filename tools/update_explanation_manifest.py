#!/usr/bin/env python3
"""Refresh public explanation metadata from local graph artifacts."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EMPEROR = Path("/Users/michael/Emperor-Palantir")
GRAPH = EMPEROR / "constellation/.understand-anything/knowledge-graph.json"
OUT = ROOT / "data/explanation-manifest.json"


def main() -> None:
    graph = json.loads(GRAPH.read_text())
    project = graph.get("project", {})
    layers = [
        {"name": layer.get("name"), "description": layer.get("description")}
        for layer in graph.get("layers", [])
    ]
    tour = [
        {
            "order": step.get("order"),
            "title": step.get("title"),
            "description": step.get("description"),
        }
        for step in graph.get("tour", [])
    ]
    node_types: dict[str, int] = {}
    for node in graph.get("nodes", []):
        kind = node.get("type", "unknown")
        node_types[kind] = node_types.get(kind, 0) + 1

    manifest = {
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": {
            "graph_path": str(GRAPH),
            "graph_analyzed_at": project.get("analyzedAt"),
            "graph_commit_hash": project.get("gitCommitHash"),
            "node_count": len(graph.get("nodes", [])),
            "edge_count": len(graph.get("edges", [])),
            "node_types": node_types,
        },
        "live_links": {
            "constellation": "/explain/constellation.html",
            "constellation_dashboard": "/explain/constellation.html",
        },
        "layers": layers,
        "tour": sorted(tour, key=lambda item: item.get("order") or 999),
        "authority_boundary": "Explanation layer only. Not contract authority, Sage authority, owner approval, field direction, or project-control validation.",
    }
    OUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
