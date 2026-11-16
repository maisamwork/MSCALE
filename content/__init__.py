import importlib

CONTENT = {}
for mod in ["c01", "c02", "c03", "c04", "c05", "c06", "c07", "c08"]:
    CONTENT.update(getattr(importlib.import_module(f".{mod}", __name__), "CONTENT"))

for mod in ["x1", "x2", "x3", "x4", "x5", "x6"]:
    for slug, x in getattr(importlib.import_module(f".{mod}", __name__), "X").items():
        c = CONTENT.setdefault(slug, {})
        if "deep" in x:
            c.setdefault("works", []).extend(x["deep"])
        if "mistakes" in x:
            c["mistakes"] = x["mistakes"]
        if "extra_faqs" in x:
            c.setdefault("faqs", []).extend(x["extra_faqs"])
        if "extra_examples" in x:
            c.setdefault("examples", []).extend(x["extra_examples"])
