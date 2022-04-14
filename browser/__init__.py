from flask import *

app = Flask(__name__)

@app.route('/')
def main():
	if 'name' not in session:
		return render_template('index.html', name=None)
	else:
		return render_template('index.html', name=[session['name']])

if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)
