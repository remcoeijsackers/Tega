from flask import Flask
from src.commands import generate_account
from flask import request

app = Flask(__name__)

@app.route("/")
def account():
    args = [i for i in request.args.keys()]

    def retrieve(name):
        if name in args:
            return request.args.get(name)
        
    return generate_account(
        mail=retrieve("mail") if retrieve("mail") else "f", 
        nationality=retrieve("nationality") if retrieve("nationality") else "r",
        gender=retrieve("gender") if retrieve("gender") else None, 
        count= retrieve("count") if retrieve("count") else 1,
        logging=retrieve("logging")
        )



if __name__ == '__main__':
    app.run()