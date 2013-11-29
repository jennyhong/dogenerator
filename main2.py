# much hungry
# very run
# such computer
# so laptop

import random
import nltk
#import io
from nltk.stem import WordNetLemmatizer

def dogify(inp):
  wnl = WordNetLemmatizer()
  l = nltk.word_tokenize(inp)
  l1, l2, l3 = [], [], []

  for i, j, in nltk.pos_tag(l):
    if len(i) < 4: continue
    if j == "NN":
      l1.append(i)
    elif j == "JJ":
      l2.append(i)
    elif j.find("VB") != -1:
      l3.append(i)

  def rnd(x):
    return random.randint(0, x-1)

  def go(l):
    l.sort()
    ret = [""]
    cnt = 0
    bst = 0
    prv = ""
    for i in l:
      if i != prv: 
        cnt = 0
      cnt += 1
      if cnt > bst:
        bst = cnt
        ret = []
      if cnt == bst:
        ret.append(i)
      prv = i
    x = rnd(len(ret))
    r = ret[x]
    return r
##    return wnl.lemmatize(r)


  noun = go(l1)
  adj = go(l2)
  verb = go(l3)

  s = ""
  if len(noun):
    s += "so " + noun + "\n"
  if len(adj):
    s += "much " + adj + "\n"
  if len(verb):
    s +=  "very " + verb + "\n"
  s += "wow"
  return s

#fp = open("sample")
s = raw_input()
print dogify(s)
