#!/usr/bin/python

import sys 

#open wiki.txt and read the first 2 words
with open('../data/wiki.txt') as f: 
    first_line = f.readline()
    m, n = first_line.split("\t",-1)
    n = n.strip("\n")

#create M.fst
letters_m = list(m)
i=0
j=len(m)
with open('../fsts/M.fst','w') as f:
    for l in letters_m:
        f.write("{}\t {}\t {}\t {}\t 0\n".format(i, i+1, l, l))
        i += 1
        if i==j:
            f.write("{}".format(i))

#create N.fst
letters_n = list(n)
i=0
j=len(n)
with open('../fsts/N.fst','w') as f:
    for l in letters_n:
        f.write("{}\t {}\t {}\t {}\t 0\n".format(i, i+1, l, l))
        i += 1
        if(i==j):
            #f.write("{}\t {}\t {}\t {}\t 0\n".format(i, i+1, 'ε', 'ε')) #from eps:eps move , then we change i to i+1 in the next line
            f.write("{}".format(i))


