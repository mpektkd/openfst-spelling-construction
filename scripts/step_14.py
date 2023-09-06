import glob
import os
import re
import numpy as np
import sklearn
from w2v_train import W2VLossLogger
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from gensim.models import KeyedVectors
from string import Template
from shutil import copy

SCRIPT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
data_dir = os.path.join(SCRIPT_DIRECTORY, "../data/aclImdb/")
train_dir = os.path.join(data_dir, "train")
test_dir = os.path.join(data_dir, "test")
pos_train_dir = os.path.join(train_dir, "pos")
neg_train_dir = os.path.join(train_dir, "neg")
pos_test_dir = os.path.join(test_dir, "pos")
neg_test_dir = os.path.join(test_dir, "neg")

# For memory limitations. These parameters fit in 8GB of RAM.
# If you have 16G of RAM you can experiment with the full dataset / W2V
#MAX_NUM_SAMPLES = 5000
# Load first 1M word embeddings. This works because GoogleNews are roughly
# sorted from most frequent to least frequent.
# It may yield much worse results for other embeddings corpora
#NUM_W2V_TO_LOAD = 1000000


SEED = 42

# Fix numpy random seed for reproducibility
np.random.seed(SEED)

#model = Word2Vec.load("../data/gutenberg_w2v.100d.model")
#model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True,limit=NUM_W2V_TO_LOAD)
def strip_punctuation(s):
    return re.sub(r"[^a-zA-Z\s]", " ", s)


def preprocess(s):
    return re.sub("\s+", " ", strip_punctuation(s).lower())


def tokenize(s):
    return s.split(" ")

                                                                #functiobn to preprocces the data as we have done at step_1
def preproc_tok(s):
    return tokenize(preprocess(s))


def read_samples(folder, preprocess=lambda x: x, MAX_NUM_SAMPLES=0):        #function to read the movie reviews and transform them to list of lists of tokens
    samples = glob.iglob(os.path.join(folder, "*.txt"))
    data = []
    
    for i, sample in enumerate(samples):
        if MAX_NUM_SAMPLES > 0 and i == MAX_NUM_SAMPLES:
            break
        with open(sample, "r") as fd:
            x = [preprocess(l) for l in fd][0]
            data.append(x)

    return data


def create_corpus(pos, neg):                        #union of pos and neg reviews to a list and creation of lebels list
    corpus = np.array(pos + neg, dtype = object)
    y = np.array([1 for _ in pos] + [0 for _ in neg])
    indices = np.arange(y.shape[0])
    np.random.shuffle(indices)                      #shuffle the indices to avoid overfitting

    return list(corpus[indices]), list(y[indices])


def extract_nbow(corpus, key, size):

    i = 0                                                       #creation of NBOW
    for sentence in corpus:
        NBOW = np.zeros(size)
        n = 0
        for token in sentence:                                   
            if token in model.wv.vocab:
                NBOW += model.wv[token] 
            else:
                NBOW += np.zeros(size)  #each OOV word is the null vector
            n+=1
        corpus[i] = NBOW/n      #NBOW = vector average of words
        i+=1
    return corpus

def train_sentiment_analysis(train_corpus, train_labels):       #we train our model
    """Train a sentiment analysis classifier using NBOW + Logistic regression"""
    X_scaled = StandardScaler().fit_transform(train_corpus)     #first we standarize the values for good performance of the classifier
    clf = LogisticRegression()
    clf.fit(X_scaled, train_labels)                                #we forward the data

    return clf

def evaluate_sentiment_analysis(classifier, test_corpus, test_labels, train_size,test_size, file):      #evaluate the classifier
    """Evaluate classifier in the test corpus and report accuracy"""
    X_scaled = StandardScaler().fit_transform(test_corpus)                                               #if the neural net has been trained with standarized value, it expects always standarized input
    file.write(temp1.substitute(train_size=train_size, test_size=test_size, result=accuracy_score(test_labels, classifier.predict(X_scaled))))

if __name__ == "__main__":
    with open('results.txt','w') as file: #we make the file our results will be stored
        temp1 = Template("The accuracy score , with $train_size pos and neg reviews for training data and $test_size for test set, is: $result\n\t")
        temp2 = Template("The results of $whose model are:\n\n\t ")
        keys = ['our', 'google_10^6', 'google_all']
        train_sizes = [5000, 12500]
        test_sizes = [3000, 7000, 12500]
        for key in keys:
            file.write(temp2.substitute(whose=key))
            if key == 'our':
                size = 100
                model = Word2Vec.load("../data/gutenberg_w2v.100d.model")
            elif key == "google_10^6":
                model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True,limit=1000000)
                size = 300
            else:
                size = 300
                model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True,limit=None)
            for train_size in train_sizes:
                #read Imdb corpus
                pos = read_samples(folder=pos_train_dir, preprocess=preproc_tok, MAX_NUM_SAMPLES=train_size)
                neg = read_samples(folder=neg_train_dir, preprocess=preproc_tok, MAX_NUM_SAMPLES=train_size)
                #create corpus and labels
                corpus, labels = create_corpus(pos,neg)
                nbow_corpus = extract_nbow(corpus, key, size)   #make the NBOWs
   
                #train / evaluate and report accuracy

                classifier = train_sentiment_analysis(nbow_corpus, labels)
                for test_size in test_sizes:
                
                    pos = read_samples(folder=pos_test_dir, preprocess=preproc_tok, MAX_NUM_SAMPLES=test_size)
                    neg = read_samples(folder=neg_test_dir, preprocess=preproc_tok, MAX_NUM_SAMPLES=test_size)
    
                    corpus, labels = create_corpus(pos,neg)
                    nbow_corpus = extract_nbow(corpus, key, size)
                    evaluate_sentiment_analysis(classifier, nbow_corpus, labels,train_size,test_size,file)
                file.write('\n')

    copy('results.txt', '../data/')
    os.remove('results.txt')