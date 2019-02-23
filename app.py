from flask import Flask, request, jsonify, url_for, redirect
from functools import wraps

app = Flask(__name__)

db = []

# This function is a decorator.
def login_required(f):
	@wraps(f)
	def verify_token(*args, **kwargs):
		print(request.args.get('token'))
		if request.args.get('token')  != "12345":
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return verify_token

@app.route("/")
def hello():
    return "RUMAD Accelerator Sample Project Backend"

@app.route("/login")
def login():
    return "login"

@app.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    if request.method == 'POST':
		transaction = {
			"type": request.args.get('type'),
			"category": request.args.get('category'),
			"amount": request.args.get('amount')
		}
		db.append(transaction.copy())
		return "SUCCESS"
    else:
        return jsonify(db)


