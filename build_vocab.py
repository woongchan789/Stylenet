import re
import pickle
from collections import Counter
import nltk

nltk.download('punkt')

class Vocab:
    '''vocabulary'''
    def __init__(self):
        self.w2i = {}
        self.i2w = {}
        self.ix = 0

    def add_word(self, word):
        if word not in self.w2i:
            self.w2i[word] = self.ix
            self.i2w[self.ix] = word
            self.ix += 1

    def __call__(self, word):
        if word not in self.w2i:
            return self.w2i['<unk>']
        return self.w2i[word]

    def __len__(self):
        return len(self.w2i)

# REVISE: romantic을 mode_list에 추가
# REVISE: vocab을 수정
# 1. factual vocab: factual_train.txt
# 2. humorous vocab: factual_train.txt + humorous.txt
# 3. romantic vocab: factual_train.txt + romantic.txt

def build_vocab(mode_list=['factual', 'humorous', 'romantic']):
    '''build vocabulary'''
    # define vocabulary
    vocab = Vocab()
    # add special tokens
    vocab.add_word('<pad>')
    vocab.add_word('<s>')
    vocab.add_word('</s>')
    vocab.add_word('<unk>')
    
    # add words

    if mode == 'factual':
        captions = extract_captions(mode='factual')
        words = nltk.tokenize.word_tokenize(captions)
        counter = Counter(words)
        words = [word for word, cnt in counter.items() if cnt >= 2]
    else:
        captions = extract_captions(mode=mode)
        words = nltk.tokenize.word_tokenize(captions)

    for word in words:
        vocab.add_word(word)

    return vocab

def extract_captions(mode='factual'):
    '''extract captions from data files for building vocabulary'''
    text = ''
    if mode == 'factual':
        with open("data/factual_train.txt", 'r') as f:
            res = f.readlines()

        r = re.compile(r'\d*.jpg#\d*')
        for line in res:
            line = r.sub('', line)
            line = line.replace('.', '')
            line = line.strip()
            text += line + ' '

    else:
        if mode == 'humorous':
            with open("data/humor/funny_train.txt", 'r') as f:
                res = f.readlines()
        else:
            with open("data/romantic/romantic_train.txt", 'r') as f:
                res = f.readlines()

        for line in res:
            line = line.replace('.', '')
            line = line.strip()
            text += line + ' '

    return text.strip().lower()

# REVISE: mode_list에 romantic 추가
if __name__ == '__main__':
    vocab = build_vocab(mode_list=['factual', 'humorous', 'romantic'])
    print(vocab.__len__())
    with open('data/vocab.pkl', 'wb') as f:
        pickle.dump(vocab, f)
