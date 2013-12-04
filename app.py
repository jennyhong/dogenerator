import collections
from flask import Flask, render_template, send_from_directory
import random
import os
import nltk
from nltk.stem import WordNetLemmatizer

# initialization
app = Flask(__name__)
app.config.update(
  DEBUG = True,
)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/dogify/<inp>")
def dogify(inp):
	wnl = WordNetLemmatizer()
	words_by_pos = findRelevantWords(inp)

	mywords = collections.defaultdict(list)
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

	return ". ".join(phrases)

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
		if pos == "NN" or pos == "JJ":
			words_by_pos[pos].append(word)
		elif pos.find("VB") != -1:
			words_by_pos["VB"].append(word)

	return words_by_pos

# launch
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
