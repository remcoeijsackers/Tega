from flask import Flask
from src.commands import generate_account

app = Flask("app")

@app.route("/")
def hello_world():
    return generate_account()

if __name__ == "__main__":
    app.run(debug=True)