#!/bin/bash

fstcompile --isymbols=chars.syms --osymbols=words.syms --keep_isymbols --keep_osymbols Union.fst Union.binfst

fstrmepsilon Union.binfst | fstdeterminize | fstminimize >V.binfst 

fstprint V.binfst >V.fst

#transfer the files in the correct directory
cp V.fst ../fsts
cp V.binfst ../fsts

rm V.fst V.binfst 
rm Union.fst words.syms chars.syms Union.binfst