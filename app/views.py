import re
from flask import render_template,request
from app import app
import joblib
import pandas as pd
from app import kgf



values={1:[79.84,47.58,39.87], 2:[77.76,48.44,19.79], 3:[40,67.77,79.92],4:[20.75,67.54,20.05],5:[20.75,67.73,20.29],6:[21.44,48.01,20.23],7:[20.99,47.28,19.87],8:[40.04,67.52,19.82],9:[18.77,68.36,19.41],10:[18.87,18.75,40.21],11:[100.73,82.01,50.05],11:[100.23,82.01,50.05],12:[20.27,27.18,29.92],13:[23.18,132.53,200],14:[99.42,17,50.22],15:[100.32,17.72,50.82],16:[20.8,134.22,199.89],17:[19.58,16.55,10.01],18:[49.88,59.05,50.04],19:[21.98,16.93,30.59],20:[117,46.24,19.56],21:[78.4,46.86,39.99],22:[101.2,28.74,29.94]}

@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/<name>")
def helloname(name):
    return f"hello {name}"


@app.route("/admin")
def reroute():
    loaded_model=joblib.load("C:\\Users\\LENOVO\\Desktop\\final_project\\Agrivate\\app\\model.joblib")
    col=["N","P","K","temperature","humidity","ph","rainfall"]
    N=[60,51,36,22.69657794,82.81088865,6.028321557999999,256.9964761]
    dic={}
    for i in range(len(col)):
      dic[col[i]]=N[i]
    print(dic)
    dataframe=pd.DataFrame(dic,index=[0])
    return(loaded_model.predict(dataframe)[0])

@app.route("/findcrop/<lat>/<long>/<n>/<p>/<k>")
def getdata(lat,long,n,p,k):
  loaded_model=joblib.load("C:\\Users\\LENOVO\\Desktop\\final_project\\Agrivate\\app\\modelNPKTH.joblib")
  val=kgf.get_temp_humidity(lat,long)
  humidity=val[0]
  temperature=val[1]-273
  dic={}
  col=["N","P","K","temperature","humidity",]
  values=[n,p,k,temperature,humidity]
  for i in range(len(col)):
      dic[col[i]]=values[i]
  dataframe=pd.DataFrame(dic,index=[0])
  return(loaded_model.predict(dataframe)[0])


@app.route("/getvalues/<cid>/<n>/<p>/<k>")
def getvalues(cid,n,p,k):
    cid=int(cid)
    values={ 1:[79.84,47.58,39.87], 2:[77.76,48.44,19.79], 3:[40,67.77,79.92],4:[20.75,67.54,20.05],5:[20.75,67.73,20.29],6:[21.44,48.01,20.23],7:[20.99,47.28,19.87],8:[40.04,67.52,19.82],9:[18.77,68.36,19.41],10:[18.87,18.75,40.21],11:[100.73,82.01,50.05],11:[100.23,82.01,50.05],12:[20.27,27.18,29.92],13:[23.18,132.53,200],14:[99.42,17,50.22],15:[100.32,17.72,50.82],16:[20.8,134.22,199.89],17:[19.58,16.55,10.01],18:[49.88,59.05,50.04],19:[21.98,16.93,30.59],20:[117,46.24,19.56],21:[78.4,46.86,39.99],22:[101.2,28.74,29.94]}
    value=values[cid]
    nret=value[0]-int(n)
    pret=value[1]-int(p)
    kret=value[2]-int(k)
    return f"{nret} {pret} {kret}"

@app.route("/predictnutrients",methods = ['POST','GET'])
def predictNutrients():
  crops=["rice","maize","chickpea","kidneybeans","pigeonpeas","mothbeans","mungbean","blackgram","lentil","pomegranate","banana","mango","grapes","watermelon","muskmelon","apple","orange","papaya","coconut","cotton","jute","coffee"]
  if  request.method == "POST":
    values={ 1:[79.84,47.58,39.87], 2:[77.76,48.44,19.79], 3:[40,67.77,79.92],4:[20.75,67.54,20.05],5:[20.75,67.73,20.29],6:[21.44,48.01,20.23],7:[20.99,47.28,19.87],8:[40.04,67.52,19.82],9:[18.77,68.36,19.41],10:[18.87,18.75,40.21],11:[100.73,82.01,50.05],11:[100.23,82.01,50.05],12:[20.27,27.18,29.92],13:[23.18,132.53,200],14:[99.42,17,50.22],15:[100.32,17.72,50.82],16:[20.8,134.22,199.89],17:[19.58,16.55,10.01],18:[49.88,59.05,50.04],19:[21.98,16.93,30.59],20:[117,46.24,19.56],21:[78.4,46.86,39.99],22:[101.2,28.74,29.94]}
    n=int(request.form['nitrogen'])
    p=int(request.form['phosphorous'])
    k=int(request.form['pottasium'])
    crop=request.form['crop']
    point=crops.index(crop) + 1
    print(point)
    value=values[point]
    nret=round(value[0]-int(n),2)
    pret=round(value[1]-int(p),2)
    kret=round(value[2]-int(k),2)
    return f"{nret} {pret} {kret}"
  else:
    return render_template("predictnutrients.html",crop = crops)


@app.route("/predictcrop",methods = ['POST','GET'])
def predict():
  if request.method == "POST":
    n=int(request.form['nitrogen'])
    p=int(request.form['phosphorous'])
    k=int(request.form['pottasium'])
    lat=float(request.form['latitude'])
    long=float(request.form['longitude'])
    print( lat , long)
    loaded_model=joblib.load("C:/Users/Neeraj Jayaraj/Desktop/Projects/Agrivate/app/modelNPKTH.joblib")
    val=kgf.get_temp_humidity(lat,long)
    humidity=val[0]
    temperature=val[1]-273
    dic={}
    col=["N","P","K","temperature","humidity",]
    values=[n,p,k,temperature,humidity]
    for i in range(len(col)):
      dic[col[i]]=values[i]
    dataframe=pd.DataFrame(dic,index=[0])
    print("here")
    return(loaded_model.predict(dataframe)[0])
  return render_template("predictcrop.html")
    