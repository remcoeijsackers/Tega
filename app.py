from flask import Flask
from src.commands import generate_account
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return generate_account()

@app.route('/account')
def account():
    count = request.args.get('count', 1)
    return generate_account(count=int(count))

if __name__ == "__main__":
    app.run(debug=True, port=9000)