#!/usr/bin/python 
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet = "ab"

# fuction that returns the weight for each arc based on the frequency we calculated
def weight(source,target,dictionary):
    for k in dictionary.keys():
        if ((source == k[2]) and (target == k[7])):     # k = ('s','t') so k[2]=s and k[7]=t
            return round((-1)*math.log(float(dictionary[k])),3) #cost
    return pow(10,5) # infinite cost


dictionary = {} #create dictionary with (source,target) : frequency from stored file
with open('../data/edits_frequency_output.txt', 'r') as f: 
    for line in f:
        k, v = line.split(" : ",-1)
        v = v.strip("\n")
        dictionary[k] = v


with open('../fsts/E.fst', 'w') as file:
    # No edit
    for l in alphabet:
        file.write("0\t 0\t {}\t {}\t 0\n".format(l, l))

    # Deletes: input character, output epsilon
    for l in alphabet:
        file.write("0\t 0\t {}\t ε\t {}\n".format(l,weight(l,'ε',dictionary)))

    # Insertions: input epsilon, output character
    for l in alphabet:
        file.write("0\t 0\t ε\t {}\t {}\n".format(l,weight('ε',l,dictionary)))

    # Substitutions: input one character, output another
    for l in alphabet:
        for r in alphabet:
            if l is not r:
                file.write("0\t 0\t {}\t {}\t {}\n".format(l, r,weight(l,r,dictionary)))

    # Final state
    file.write('0')
