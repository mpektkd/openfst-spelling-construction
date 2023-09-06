#!/usr/bin/env bash

# Run shortest path to get the edits for the minimum edit distance
fstshortestpath ../fsts/MLN.binfst | 
# Print the shortest path fst
fstprint --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --show_weight_one |
# Ignore the accepting state and arcs with 0 weight (no edits)
grep -v "0$" |
# Get columns 3 and 4 that contain source and destination symbol for the remaining columns (edits) 
cut -d$'\t' -f3-4
