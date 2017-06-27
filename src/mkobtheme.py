#!/usr/bin/env python
# Generate differents themerc from a single rc file by calling mkrc.py

import subprocess
import sys

themes = {}

if sys.argv[1]:
    fname = sys.argv[1]
else:
    fname = 'src/rc'

if sys.argv[2]:
    mkrc = ('python', sys.argv[2])
else:
    mkrc = ('python', 'src/mkrc.py')

if sys.argv[3]:
    themename = sys.argv[3]
else:
    themename = 'retrosmart-openbox'

with open(fname) as f:
    for line in f:
        if not line.strip():
            continue
        else:
            k, v = line.split('=')
            themes[k.strip()] = v.strip()

for t in themes:
    dname = themename + '-' + t
    dnameb = themename + '-' + t + '-nobuttons'
    md = ('mkdir', dname)
    mdb = ('mkdir', dnameb)
    subprocess.call(md)
    subprocess.call(mdb)
    f = dname + '/themerc'
    fb = dnameb + '/themerc'
    if ':' in themes[t]:
        active, menu = themes[t].split(':')
        active = '#' + active
        menu = '#' + menu

        mkt = (mkrc[0], mkrc[1], '-a', active, '-m', menu)
        mktb = (mkrc[0], mkrc[1], '-C', '-a', active, '-m', menu)
    else:
        active = '#' + themes[t]
        mkt = (mkrc[0], mkrc[1], '-a', active)
        mktb = (mkrc[0], mkrc[1], '-C', '-a', active)
    with open(f, "w") as outfile:
        subprocess.call(mkt, stdout=outfile)
    with open(fb, "w") as outfile:
        subprocess.call(mktb, stdout=outfile)

