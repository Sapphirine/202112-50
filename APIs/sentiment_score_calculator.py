import pandas as pd
import numpy as np
import re
from flair.models import TextClassifier
from flair.data import Sentence
sia = TextClassifier.load('en-sentiment')


def get_sentiment(s,flag):
  if flag:
    if "POSITIVE" in  s:
      return "POSITIVE"
    else:
      return "NEGATIVE"
  else:
    if "POSITIVE" in  s:
      return +1.0*float(s[s.find('(')+1:s.find(')')])
    else:
      return -1.0*float(s[s.find('(')+1:s.find(')')])

def sentiment_score(x):
    sentence = Sentence(x)
    sia.predict(sentence)
    score = sentence.labels[0]
    return score

