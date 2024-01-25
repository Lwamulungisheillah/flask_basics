from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return " Introduction To Flask Mastery Series "

if __name__ == "__main__":
    app.run(debug=True)
