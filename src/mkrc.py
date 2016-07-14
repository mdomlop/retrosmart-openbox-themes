#!/usr/bin/env python
import subprocess


fname = 'rc'
themes = {}

with open(fname) as f:
    for line in f:
        if not line.strip():
            continue
        else:
            k, v = line.split('=')
            themes[k.strip()] = v.strip()

for t in themes:
    dname = 'retrosmart-openbox-' + t
    dnameb = 'retrosmart-openbox-' + t + '-nobuttons'
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

        mkt = ('mkobtheme.py', '-a', active, '-m', menu)
        mktb = ('mkobtheme.py', '-C', '-a', active, '-m', menu)
    else:
        active = '#' + themes[t]
        mkt = ('mkobtheme.py', '-a', active)
        mktb = ('mkobtheme.py', '-C', '-a', active)
    with open(f, "w") as outfile:
        subprocess.call(mkt, stdout=outfile)
    with open(fb, "w") as outfile:
        subprocess.call(mktb, stdout=outfile)

