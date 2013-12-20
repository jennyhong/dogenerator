import dogify
from flask import Flask, render_template, send_from_directory
import json
import os
from StringIO import StringIO

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

@app.route('/dogify/<inp>')
def doge(inp):
	return json.dumps(dogify.dogify(inp))

# launch
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
