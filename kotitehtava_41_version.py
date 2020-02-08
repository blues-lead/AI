# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:32:02 2020

@author: Anton
"""

import re
from collections import Counter

def generate_ngram(text, count):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9]', ' ', text)
    voc = [word for word in text.split(" ") if word != ""]
    ngram = zip(*[voc[i:] for i in range(count)])
    return [" ".join(word) for word in ngram]
    
with open('some_book.txt','r') as fl:
    text = fl.read()

for i in range(1,4):
    test = generate_ngram(text, i)
    test = Counter(test)
    
    word, freq = zip(*test.items())
    iS = np.argsort(freq)[::-1]
    wrds = np.array(word)[iS]
    vals = np.array(freq)[iS]
    
    print()
    print(i,"GRAM TEXT!")
    s = " ".join([choices(wrds, vals)[0] for i in range(100)])
    print(s)
