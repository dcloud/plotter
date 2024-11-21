#!/bin/sh

vpype read "$1" linemerge linesort reloop linesimplify \
    layout --fit-to-margins 0.25in letter \
    write -p letter \
    "%prop.vp_source.with_stem(prop.vp_source.stem + '_processed')%"
