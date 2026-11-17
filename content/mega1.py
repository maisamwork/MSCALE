# -*- coding: utf-8 -*-
from .mega1a import CONV, conv_article, conv_body
from .mega1b import CALC, calc_article, calc_body

MEGA = {}
CONTENT = {}
for f in CONV:
    slug, fn, fs, tn, ts = f[0], f[1], f[2], f[3], f[4]
    MEGA[slug] = {"name": f"{fn} to {tn} Converter", "cat": "Converters", "short": f[7],
                  "body": conv_body(f), "desc": f"{f[7]}. Exact defined factors, instant results, swap direction and a reference table \u2014 runs entirely in your browser."}
    CONTENT[slug] = conv_article(f)
for f in CALC:
    slug, name, short = f[0], f[1], f[2]
    MEGA[slug] = {"name": name, "cat": "Calculators", "short": short,
                  "body": calc_body(f), "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT[slug] = calc_article(f)
