from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bievenidos a mi primera API con flask"

app.run(debug=True)