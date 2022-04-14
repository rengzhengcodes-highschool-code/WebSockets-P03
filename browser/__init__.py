from flask import *

app = Flask(__name__)

@app.route('/')
def main():
	if 'user' not in session:
		return render_template('index.html', user=None)
	else:
		return render_template('index.html', user=[session['user']])

if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)
