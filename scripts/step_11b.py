#!/usr/bin/python

import sys 
import math
from shutil import copy
import os
import string

#create dictionary that has as key the word and as values the # of appearance
dict = {}
with open("../data/en_50k.txt", "r") as file:
    for line in file:
        k, v = line.split(" ",-1)
        v = v.strip("\n")
        dict[k] = v 

printset = set(string.printable) #create set with printable ascii characters
dict2 = {}  # create 2nd dictionary to save word to be erased
for k in dict.keys():
  isprintable = set(k).issubset(printset)   #check if word is printable
  if not isprintable:
    dict2[k] = 0 #if not printable save in dict2

for k in dict2.keys():
  dict.pop(k)   #and erase them

F = 0
for v in dict.values():
    F += int(v)  #calculate the sum of values

with open('../fsts/W_en_50k.fst', 'w') as file:
    for k in dict.keys(): #constract all:all/freq
        file.write("0\t 0\t {}\t {}\t {}\n".format(k, k, round((-1)*math.log(float(dict[k])/F),3)))
    # Final state
    file.write('0')


dic_2 = {} #new dictionary with diffrent number (starting from 0) for each word
dic_2['ε'] = 0  #add <eps> in dic
i = 1   #save 0 position to add <eps> 
for word in dict.keys():
    dic_2[word] = i
    i += 1

#print(dic_2) #print for check

with open('../vocab/words_en_50k.syms','w') as file:    #save new dictionary in 'wordsen_50k.syms'
    for k, v in dic_2.items():
        file.write("{}\t {}\n".format(k, v))



dic = {}
#open the file words_en_50k.syms from the correct directory
#with open("my_lex.txt", "r") as file:    
with open("../vocab/words_en_50k.syms", "r") as file:
    for line in file:
        k, v = line.split(" ",1)                #split the words
        k = k.strip("\t")                       #abstract tabs from the first one
        v = int(v.strip("\n"))                  #abstract newlines from the second one and make it integer
        dic[k] = v                              #add each word with her encoding in the dic
    copy("../vocab/words_en_50k.syms", '.')   #copy the necessary files
    copy("../vocab/chars.syms", '.')



#we have to make 15k automata in order to being used in the bash script 
from string import Template 
t1 = Template('$src $dst $input $output ' + str(0) + '\n')                  #we use templates

#we make the union of automata
with open("Union.fst", "w") as f:
    i = 2
    for word in dic.keys():
        if word == "ε":
            continue
      #we write src dst input output weight for each word
                                                                                           #we give the output when the first character is given
        if len(word) != 1:
            f.write(t1.substitute(src = str(0), dst = str(i), input = word[0], output = word))
            for ch in word[1:-1]:
                f.write(t1.substitute(src = str(i), dst = str(i+1), input = ch, output = "ε"))          #the output for the every next transition is "ε"
                i += 1 
            f.write(t1.substitute(src = str(i), dst = str(1), input = word[-1], output = "ε"))
            i += 1
        #if len(word) == 1 then go to q=1
        
        else:
            f.write(t1.substitute(src = str(0), dst = str(1), input = word[-1], output = word))
    f.write(str(1))

