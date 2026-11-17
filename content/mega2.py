# -*- coding: utf-8 -*-
from .mega2b import MEGA2, CONTENT2

MEGA = {}
CONTENT = {}
for slug, m in MEGA2.items():
    MEGA[slug] = {"name": m["name"], "cat": m["cat"], "short": m["short"], "body": m["body"],
                  "desc": m["short"] + ". Free, instant and entirely in your browser \u2014 nothing is uploaded."}
    CONTENT[slug] = CONTENT2[slug]
