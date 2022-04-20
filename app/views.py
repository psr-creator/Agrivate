from flask import render_template
from app import app

@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/<name>")
def helloname(name):
    return f"hello {name}"


@app.route("/admin")
def reroute():
    return "admin"