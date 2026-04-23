from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Muraho! Iyi ni cloud app yanjye"

if __name__ == "__main__":
    app.run(debug=True)