#!/usr/bin/python

import re
import sys

import contractions
import nltk


def download_corpus(corpus="gutenberg"):
    """Download Project Gutenberg corpus, consisting of 18 classic books
    Book list:
       ['austen-emma.txt',
        'austen-persuasion.txt',
        'austen-sense.txt',
        'bible-kjv.txt',
        'blake-poems.txt',
        'bryant-stories.txt',
        'burgess-busterbrown.txt',
        'carroll-alice.txt',
        'chesterton-ball.txt',
        'chesterton-brown.txt',
        'chesterton-thursday.txt',
        'edgeworth-parents.txt',
        'melville-moby_dick.txt',
        'milton-paradise.txt',
        'shakespeare-caesar.txt',
        'shakespeare-hamlet.txt',
        'shakespeare-macbeth.txt',
        'whitman-leaves.txt']
    """
    nltk.download(corpus)
    raw = nltk.corpus.__getattr__(corpus).raw()

    return raw


def identity_preprocess(s):
    return s


def clean_text(s):
    s = s.strip()  # strip leading / trailing spaces
    s = s.lower()  # convert to lowercase
    s = contractions.fix(s)  # e.g. don't -> do not, you're -> you are
    s = re.sub("\s+", " ", s)  # strip multiple whitespace
    s = re.sub(r"[^a-z\s]", " ", s)  # keep only lowercase letters and spaces

    return s


def tokenize(s):
    tokenized = [w for w in s.split(" ") if len(w) > 0]  # Ignore empty string

    return tokenized


def preprocess(s):
    return tokenize(clean_text(s))


def process_file(corpus, preprocess=identity_preprocess):
    lines = [preprocess(ln) for ln in corpus.split("\n")]
    lines = [ln for ln in lines if len(ln) > 0]  # Ignore empty lines

    return lines


if __name__ == "__main__":
    CORPUS = sys.argv[1] if len(sys.argv) > 1 else "gutenberg"
    raw_corpus = download_corpus(corpus=CORPUS)
    preprocessed = process_file(raw_corpus, preprocess=preprocess)

    #for words in preprocessed:
    #    sys.stdout.write(" ".join(words))
    #    sys.stdout.write("\n")

# ***ERVTHMA A*** #
dictionary = {} #create dictionary, in which to put the tokens
for line in preprocessed:
    for word in line:
        if word not in dictionary.keys():
            dictionary[word] = 0 #add to dictionary and initialize with value 0
        dictionary[word] += 1 # value += 1 for every copy

#print(dictionary) #check if the output is correct

# ***ERVTHMA B*** #
erase = {} #create a new dir to save words to be erased
for word in dictionary.keys():
    if dictionary[word] < 5:
        erase[word]=0

for word in erase.keys(): #erase these words
    dictionary.pop(word)

#print(dictionary) #check if the output is correct

# ***ERVTHMA C*** #
with open('../vocab/words.vocab.txt','w') as file:
    for k, v in dictionary.items():
        file.write("{}\t {}\n".format(k, v))
