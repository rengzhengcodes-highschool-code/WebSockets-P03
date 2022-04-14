from flask import *
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(64)

@app.route('/', methods=["GET"])
def main():
	if 'user' not in session:
		return render_template('index.html', user=None)
	else:
		return render_template('index.html', user=session['user'])

@app.route('/login', methods=["POST"])
def login():
	if 'user' not in session:
		session['user']=request.form['username']
		return redirect('/')
	else:
		return redirect('/')

if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)
