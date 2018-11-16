import tweepy
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from textblob import TextBlob
from textblob import Word
import nltk
'''nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')'''

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.tags,wiki.noun_phrases)
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)
zen = TextBlob("Beautiful is better than ugly. "
               "Explicit is better than implicit. "
               "Simple is better than complex.")
print(zen.words,zen.sentences)
w=Word('Cats')
v=Word('went')
print(w.lemmatize())
print(v.lemmatize('v'))
for sentence in zen.sentences:
    print(sentence.sentiment)
b = TextBlob("I havv goood speling!")
print(b.correct())
w1 = Word('falibility')
print(w1.spellcheck())
monty = TextBlob("We are no longer the Knights who say Ni. "
                 "We are now the Knights who say Ekki ekki ekki PTANG.")
print(monty.word_counts['ekki'])
print(monty.words.count('ekki'))
print(monty.words.count('ekki',case_sensitive=True))
en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(to='es'))
chinese_blob = TextBlob(u"美丽优于丑陋")
print(chinese_blob.translate(from_lang="zh-CN", to='en'))
b = TextBlob(u"بسيط هو أفضل من مجمع")
print(b.detect_language())
print(zen[0:19])
print(zen.upper())
apple_blob = TextBlob('apples')
banana_blob = TextBlob('bananas')
print(apple_blob + ' and ' + banana_blob)
print("{0} and {1}".format(apple_blob, banana_blob))

