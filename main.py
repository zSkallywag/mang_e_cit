from flask import Flask, render_template, request, send_file, redirect, session, g
from flask_compress import Compress


# QUI CI SARA' IL BACK END PER LA GESTIONE DEGLI INPUT






#Flask carica l'interfaccia(index.html), bisogna aggiustarla (css, html, js)
compress=Compress()#comprime i pacchetti per maggiori performance
app = Flask(__name__)
compress.init_app(app)
app.secret_key = "key"

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")
if __name__ == "__main__":
    context=('cert.pem', 'key.pem')
    app.run(debug=True)