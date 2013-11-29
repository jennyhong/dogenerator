from flask import Flask, render_template, send_from_directory
import random
import os
import nltk
# from nltk.stem import WordNetLemmatizer

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

@app.route("/dogify/<inp>")
def dogify(inp):
	l = nltk.word_tokenize(inp)
	l1, l2, l3 = [], [], []

	for i, j in nltk.pos_tag(l):
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
		return ret[x]

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

# launch
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
