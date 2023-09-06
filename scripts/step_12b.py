import logging
import multiprocessing
import os
import step_1
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from shutil import copy

# Enable gensim logging
logging.basicConfig(
    format="%(levelname)s - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)



class W2VLossLogger(CallbackAny2Vec):
    """Callback to print loss after each epoch
    use by passing model.train(..., callbacks=[W2VLossLogger()])
    """

    def __init__(self):
        self.epoch = 0

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()

        if self.epoch == 0:
            print("Loss after epoch {}: {}".format(self.epoch, loss))
        else:
            print(
                "Loss after epoch {}: {}".format(
                    self.epoch, loss - self.loss_previous_step
                )
            )
        self.epoch += 1
        self.loss_previous_step = loss


def train_w2v_model(
    sentences,
    output_file,
    window=5,
    embedding_dim=100,
    epochs=300,
    min_word_count=10,
    sg=0
):
    """Train a word2vec model based on given sentences.
    Args:
        sentences list[list[str]]: List of sentences. Each element contains a list with the words
            in the current sentence
        output_file (str): Path to save the trained w2v model
        window (int): w2v context size
        embedding_dim (int): w2v vector dimension
        epochs (int): How many epochs should the training run
        min_word_count (int): Ignore words that appear less than min_word_count times
    """
    workers = multiprocessing.cpu_count()

    # : Instantiate gensim.models.Word2Vec class
    # : Build model vocabulary using sentences
    model = Word2Vec(sentences=sentences, size=embedding_dim, window=window, min_count=min_word_count, workers=workers,callbacks=[W2VLossLogger()],sg=sg)     #we pass the parameters
    # : Train word2vec model
    model.train(sentences=sentences,epochs=epochs,total_examples=model.corpus_count,total_words=model.corpus_total_words)       #train the model
    # Save trained model
    model.save(output_file)         #save model in the output file

    return model


if __name__ == "__main__":
    # read data/gutenberg.txt in the expected format
    CORPUS = "gutenberg"
    raw_corpus = step_1.download_corpus(corpus=CORPUS)          #download corpus
    sentences = step_1.process_file(raw_corpus, preprocess=step_1.preprocess)   #after import step_1, preprocces the corpus and make list of lists of tokens
    output_file = "gutenberg_w2v.100d.model"
    window = 5
    #window = 2
    #window = 10
    embedding_dim = 100         #we have produced several models of different parameters
    #embedding_dim = 300
    epochs = 1000
    #min_word_count = 20
    min_word_count = 10
    #sg=1
    sg = 0
    train_w2v_model(
        sentences,
        output_file,
        window=window,
        embedding_dim=embedding_dim,
        epochs=epochs,
        min_word_count=min_word_count,
        sg=sg
    )
  
    copy(output_file, '../data')
    os.remove(output_file)