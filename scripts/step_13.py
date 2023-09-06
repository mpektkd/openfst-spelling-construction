import os
from step_12b import W2VLossLogger
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from string import Template 
from shutil import copy

#first we load our model
model = Word2Vec.load("../data/gutenberg_w2v.100d.model")
labels = []
tokens = []

for word in model.wv.vocab:
    tokens.append(model.wv[word])
    labels.append(word)

temp = Template('$dimi\t')
#we make the necessary files
with open('embeddings.tsv', 'w') as file:
    for vector in tokens:
        for dimi in vector:
            file.write(temp.substitute(dimi = dimi))
        file.write('\n')


with open('metadata.tsv', 'w') as file:
    for word in labels:
        file.write(word + '\n')

copy('embeddings.tsv', '../data')
copy('metadata.tsv', '../data')

os.remove('embeddings.tsv')
os.remove('metadata.tsv')