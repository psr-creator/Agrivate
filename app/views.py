from flask import render_template
from app import app

@app.route("/")
def mainPage():
  
  return render_template("index.html")

@app.route("/form2")
def helloname():
  crop = ["rice","wheat"]
  return render_template("form2.html",crop = crop)


@app.route("/form")
def reroute():
    return render_template("form.html")