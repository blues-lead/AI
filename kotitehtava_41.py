# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:43:20 2020

@author: Anton
"""
import re
import nltk.corpus
from nltk.corpus import brown
import pickle
from collections import Counter
import random
import numpy as np

class Ngram:
    def __init__(self, n, corps_obj):
        self.n = n
        self.obj = corps_obj
        self.sentencies = []
        self.__preprocess_text1()
        self.unigrams = Counter()
        [self.unigrams.update(Counter(word)) for word in self.sentencies]
        self.ngrams = Counter()
        self.nm1grams = Counter()
        self.__extract_ngrams()
        self.list_ngrams
        
    def get_ngram(self):
        return self.list_ngrams
        
    def max_prob(self, prior):
        probs = {}
        den = self.nm1grams[prior]
        if den == 0:
            return random.choice(list(self.unigrams.keys()))
        if self.n < 2:
            return
        for word in self.unigrams:
            new_key = prior + " " + word
            probs[word] = self.ngrams[new_key]/self.nm1grams[prior]
        return max(probs, key=probs.get) # return key by max value
            
                
        
    def __extract_ngrams(self):
        # [" ".join(tst1[i:i+3:1]) for i in range(len(tst1)-2)]
        if self.n < 2:
            return
        elif self.n == 2:
            for sentence in self.sentencies:
                temp = [" ".join(sentence[i:i+2:1]) for i in range(len(sentence)-1)]
                self.list_ngrams = temp
                self.ngrams.update(Counter(temp))
            self.nm1grams = self.unigrams
        elif self.n > 2:
            for sentence in self.sentencies:
                temp = [" ".join(sentence[i:i+self.n:1]) for i in range(len(sentence)-(self.n - 1))]
                self.list_ngrams = temp
                self.ngrams.update(Counter(temp))
                temp = [" ".join(sentence[i:i+(self.n)-1:1]) for i in range(len(sentence)-(self.n - 2))]
                self.nm1grams.update(Counter(temp))
        return
    
    def __preprocess_text(self):
        text = ""
        i = 0
        for file in self.obj.fileids():
            for word in self.obj.sents(file):
                sentence = " ".join(word)
                if i<=100:
                    text += ". " + sentence
                    i += 1
                s = re.sub('[^a-zA-Z0-9\s\.\,]','',sentence)
                s = re.sub('\s{2,}',' ', s)
                s = s.lower()
                if len(s.split(" ")) < self.n:
                    continue
                self.sentencies.append(s.split(" "))
        with open('test_text.txt', 'w') as fl:
            print("Writing file test")
            fl.write(text)


    def __preprocess_text1(self):
        text = ""
        i = 0
        for word in self.obj.sents(categories='editorial'):
            sentence = " ".join(word)
            text += ". " + sentence
            s = re.sub('[^a-zA-Z0-9\s\.\,]','',sentence)
            s = re.sub('\s\s+',' ', s) # filter whitespaces
            s = re.sub('^\W\s*','',s) # filter marks at start
            s = re.sub('\s*[\;\'\,\`]\s*[\;\'\,\`]+','',s) # filter double marks
            s = s.lower()
            if len(s.split(" ")) < self.n:
                continue
            self.sentencies.append(s.split(" "))
#        with open('test_text.txt', 'w') as fl:
#            print("Writing file")
#            fl.write(text)
#%%
ngrams = Ngram(2, brown)
print(ngrams.get_ngram()) # print 3gram
#%%
with open('some_book.txt','r') as fl:
    text = fl.read()
