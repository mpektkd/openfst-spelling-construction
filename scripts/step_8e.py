#!/usr/bin/python

import re
import sys

dictionary = {} #create dectiorary (source,target): frequency
with open('../data/word_edits_output.txt') as f:     #open file with edits
    for line in f:  #read all lines
        s, t = line.split("\t",-1)  #split the chars (s,t) in each line
        t = t.strip("\n")
        key = (s,t)    # create tuple with key
        if key not in dictionary.keys():
            dictionary[key] = 0     #first appearance, initialize with value 0
        dictionary[key] += 1    #value += 1 for every copy

F = 0
for v in dictionary.values():
    F += v  #calculate the sum of values

with open("../data/edits_frequency_output.txt","a") as q:   #store freq (v/F) into file edits_frequency_output.txt
    for k, v in dictionary.items():
        q.write("{} : {}\n".format(k, v/F))


