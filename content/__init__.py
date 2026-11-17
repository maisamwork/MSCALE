import importlib

CONTENT = {}
for mod in ["c01", "c02", "c03", "c04", "c05", "c06", "c07", "c08", "c09", "c10", "c11", "c12", "c13"]:
    CONTENT.update(getattr(importlib.import_module(f".{mod}", __name__), "CONTENT"))

for mod in ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9"]:
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

from .mega1 import MEGA as _MEGA1, CONTENT as _CONTENT1
from .mega2 import MEGA as _MEGA2, CONTENT as _CONTENT2
from .mega3 import MEGA3 as _MEGA3, CONTENT3 as _CONTENT3

CONTENT.update(_CONTENT1)
CONTENT.update(_CONTENT2)
CONTENT.update(_CONTENT3)

MEGA = {}
MEGA.update(_MEGA1)
MEGA.update(_MEGA2)
MEGA.update(_MEGA3)
