from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def home():
    return "home page"


@app.route("/test")
def testroute():
    return "success in test route"


if __name__=="__main__":
    app.run(host='localhost')