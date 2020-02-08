# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:15:07 2020

@author: Anton
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import re
#%%
cgram = 2

def generate_ngram(text, count):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9]', ' ', text)
    voc = np.array([word for word in text.split(" ") if word != ""])
    ngram = zip(*[voc[i:] for i in range(count)])
    return [" ".join(word) for word in ngram]
#%%
def preprocess_data(txtbook, count):
    print("Preprocess data")
    with open(txtbook[0],'r', encoding='utf-8') as benf:
        brit = benf.read()
    
    with open(txtbook[1],'r', encoding='utf-8') as usnf:
        us = usnf.read()
    
    brit_grams = generate_ngram(brit,count)
    us_grams = generate_ngram(us,count)




    X = np.concatenate((brit_grams, us_grams))
    y = np.concatenate((np.zeros(len(brit_grams)), np.ones(len(us_grams))))
    return X, y

#%% Training/testing one book
X,y = preprocess_data(['beng_book.txt','us_book.txt'], cgram)

mdl = Pipeline([('vector',CountVectorizer()),
                ('tft',TfidfTransformer()),
                ('neighbor',KNeighborsClassifier())])
    
xtrain, xtest, ytrain, ytest = train_test_split(X,y,test_size = 0.2, train_size=0.8)

print("Training started")
mdl.fit(xtrain,ytrain)

print("Checking model")
prediction = mdl.predict(xtest)
print("Test set accuracy")
print(np.mean(prediction==ytest))
#%% Testing einstein and medicine books
print("Let's check book of Einstein about Special Theory of Relativity and medicine book")
X,y = preprocess_data(['einstein_relativity_theory.txt', 'medicine_book.txt'], cgram)
print('Checking')
prediction = mdl.predict(X)
print(np.mean(prediction==y))


