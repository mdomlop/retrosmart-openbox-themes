#!/bin/sh
srcdir='src/openbox'
destdir='retrosmart-openbox-themes'

for i in "$srcdir"/retrosmart-*
do
    name=$(basename $i)
    dir="$destdir/$name"/openbox-3
    mkdir -p "$dir"
    cp "$i"/themerc "$dir"/
    cp "$srcdir"/pixmaps/* "$dir"
done

