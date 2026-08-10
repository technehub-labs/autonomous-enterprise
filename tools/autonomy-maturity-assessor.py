#!/usr/bin/env python3
"""
autonomy-maturity-assessor — stub.

Reads a JSON manifest of capabilities (with current lifecycle stage) and
emits a maturity report per organizational unit. Stub only: validates input
shape and emits placeholder report.

Dimensions:
  zoom=enterprise,zoom=capability
  unit=governance
  lifecycle=*
  governance=*

Usage:
    python tools/autonomy-maturity-assessor.py <manifest.json>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

STAGES = ["assisted", "augmented", "supervised", "autonomous", "self-evolving"]


def assess(manifest: dict) -> dict:
    """Stub assessment. Replace with real scoring later."""
    units = manifest.get("organizational_units", [])
    report = {"units": [], "stages_referenced": STAGES, "stub": True}
    for unit in units:
        caps = unit.get("capabilities", [])
        report["units"].append(
            {
                "unit": unit.get("name"),
                "capability_count": len(caps),
                "stages_present": sorted(
                    {c.get("lifecycle", "unknown") for c in caps}
                ),
            }
        )
    return report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: autonomy-maturity-assessor.py <manifest.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"manifest not found: {path}", file=sys.stderr)
        return 2
    manifest = json.loads(path.read_text())
    report = assess(manifest)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
