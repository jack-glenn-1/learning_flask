from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world, index"

@app.route("/mike")
def mike():
    return "hello world, mike"

if __name__ == "__main__":
    app.run(debug=True)
