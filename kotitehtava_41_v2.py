# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:06:46 2020

@author: Anton
"""

from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob


blob = TextBlob(text)
grams = blob.ngrams(2)
print(grams)