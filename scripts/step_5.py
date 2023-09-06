#!/usr/bin/python

import sys 
import os
from shutil import copy

dic = {}
#open the file words.syms from the correct directory
#with open("my_lex.txt", "r") as file:    
with open("../vocab/words.syms", "r") as file:
    for line in file:
        k, v = line.split(" ",1)                #split the words
        k = k.strip("\t")                       #abstract tabs from the first one
        v = int(v.strip("\n"))                  #abstract newlines from the second one and make it integer
        dic[k] = v                              #add each word with her encoding in the dic
    copy("../vocab/words.syms", '.')   #copy the necessary files
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
            f.write(t1.substitute(src = str(0), dst = str(1), input = word[-1], output = word))     #we pay attention for the articles
    f.write(str(1))


