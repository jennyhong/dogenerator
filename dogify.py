import collections
import nltk
from nltk.stem import WordNetLemmatizer
import random
import string

def dogify(inp):
  """
  Given the user's input text inp, generates a list of
  doge strings, eg. ['wow', 'very text']
  """
  wnl = WordNetLemmatizer()
  words_by_pos = findRelevantWords(inp)

  mywords = collections.defaultdict(set)
  prefs = collections.defaultdict(list)
  phrases = []

  for key in words_by_pos:
    random.shuffle(words_by_pos[key])

  mywords["nouns"] = shortlist(words_by_pos["NN"])
  mywords["adjs"] = shortlist(words_by_pos["JJ"])
  mywords["verbs"] = shortlist(words_by_pos["VB"])

  prefs["nouns"] = ["such", "so", "very"]
  prefs["adjs"] = ["much", "such"]
  prefs["verbs"] = ["such", "so", "very"]

  dogewords = ["wow", "pls"]

  for key in mywords:
    for word in mywords[key]:
      pref = random.choice(prefs[key])
      w = wnl.lemmatize(word)
      phrases.append(pref + " " + w)
  random.shuffle(phrases)
  phrases = phrases[:4]

  for i in random.sample(xrange(len(phrases) - 1), max(len(phrases) / 5, 1)):
    phrases.insert(i, random.choice(dogewords))

  phrases.append("wow")
  return phrases

def shortlist(tocut, minimum=3):
  maxlen = max(len(tocut) / 3, minimum)
  return tocut[:maxlen]

def findRelevantWords(inp):
  """
  Takes in a string and returns a dict from POS to lists
  of words
  """
  allwords = nltk.word_tokenize(inp)
  words_by_pos = collections.defaultdict(list)

  for word, pos in nltk.pos_tag(allwords):
    if len(word) < 4: continue
    for desiredpos in ["NN", "JJ", "VB"]:
      if pos.find(desiredpos) != -1:
        words_by_pos[desiredpos].append(word.lower().strip(string.punctuation))

  return words_by_pos