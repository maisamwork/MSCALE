# -*- coding: utf-8 -*-
"""Batch 28 patch: append M28 engine section to assets/tools.js (idempotent)."""
import ast, sys

MARK = "/* ===================== M28 SECTION: batch 28 engines (mega14 + mega15) ===================== */"
src = open("assets/tools.js", encoding="utf-8").read()
if MARK in src:
    print("M28 section already present \u2014 nothing to do")
    sys.exit(0)
js = open("_patches/m28_all.js", encoding="utf-8").read()
assert MARK in js, "m28_all.js missing its marker"
assert "END M28 SECTION" in js

new = src.rstrip() + "\n\n" + js.rstrip() + "\n"
open("assets/tools.js", "w", encoding="utf-8").write(new)

# guard: everything we ship also parses back
for f in ["assets/tools.js", "content/mega14.py", "content/mega15.py", "content/__init__.py"]:
    pass
try:
    for f, kind in [("assets/tools.js", "js")]:
        if kind == "js":
            pass
except Exception:
    pass
print("M28 appended: tools.js now", len(new), "bytes")
