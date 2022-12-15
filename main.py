from flask import Flask, render_template, request, send_file, redirect, session, g










app = Flask(__name__)
app.secret_key = "key"

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/index", methods=["POST", "GET"])
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")