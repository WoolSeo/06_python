from flask import Flask
app = Flask(__name__)

@app.route("/kakao")
def hello():
    return "hihi"

if __name__ == "__main__":
    app.run()
