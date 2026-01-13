from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! "

@app.route("/sobre")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)