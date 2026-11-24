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
from .mega4 import MEGA4 as _MEGA4, CONTENT4 as _CONTENT4
from .mega5 import MEGA5 as _MEGA5, CONTENT5 as _CONTENT5
from .mega6 import MEGA6 as _MEGA6, CONTENT6 as _CONTENT6

CONTENT.update(_CONTENT1)
CONTENT.update(_CONTENT2)
CONTENT.update(_CONTENT3)
CONTENT.update(_CONTENT4)
CONTENT.update(_CONTENT5)
CONTENT.update(_CONTENT6)

MEGA = {}
MEGA.update(_MEGA1)
MEGA.update(_MEGA2)
MEGA.update(_MEGA3)
MEGA.update(_MEGA4)
MEGA.update(_MEGA5)
MEGA.update(_MEGA6)

from .mega7 import MEGA7 as _MEGA7, CONTENT7 as _CONTENT7
CONTENT.update(_CONTENT7)
MEGA.update(_MEGA7)

from .mega8 import MEGA8 as _MEGA8, CONTENT8 as _CONTENT8
CONTENT.update(_CONTENT8)
MEGA.update(_MEGA8)

from .mega9 import MEGA9 as _MEGA9, CONTENT9 as _CONTENT9
CONTENT.update(_CONTENT9)
MEGA.update(_MEGA9)

from .mega10 import MEGA10 as _MEGA10, CONTENT10 as _CONTENT10
CONTENT.update(_CONTENT10)
MEGA.update(_MEGA10)

from .mega11 import MEGA11 as _MEGA11, CONTENT11 as _CONTENT11
CONTENT.update(_CONTENT11)
MEGA.update(_MEGA11)

from .blog_meta import BLOG_META as _BMETA, LENGTH_RANGES as _LR, enriched_blocks as _eb, geo_checks as _gc
BLOG_META = _BMETA
LENGTH_RANGES = _LR
blog_enriched_blocks = _eb
blog_geo_checks = _gc
