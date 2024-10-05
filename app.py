from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np

model = genai.GenerativeModel("gemini-1.5-flash")
api = os.getenv("makersuite")
genai.configure(api_key="AIzaSyDJ_1xffNQGjff7ZK4XLHpaEnhThrptDus")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction_DBS",methods=["GET","POST"])
def prediction_DBS():
    return(render_template("prediction_DBS.html"))

@app.route("/prediction_result_DBS",methods=["GET","POST"])
def prediction_result_DBS():
    q = float(request.form.get("q"))
    r = (-50.6 * q ) + 90.2
    return(render_template("prediction_result_DBS.html",r=r))

@app.route("/predict_credibility",methods=["GET","POST"])
def predict_credibility():
    return(render_template("predict_credibility.html"))

@app.route("/predict_credibility_result",methods=["GET","POST"])
def predict_credibility_result():
    q = float(request.form.get("q"))
    r = (-0.0001269 * q ) + 1.29761929
    r = np.where(r>=0.5,"Creditable","Not Creditable")
    return(render_template("predict_credibility_result.html",r=r))

@app.route("/faq",methods=["GET","POST"])
def faq():
    return(render_template("faq.html"))

@app.route("/q1",methods=["GET","POST"])
def q1():
    r = model.generate_content("How should i diversify my investment porfolio?")
    return(render_template("q1_reply.html",r=r))

@app.route("/q2",methods=["GET","POST"])
def q2():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("q2_reply.html",r=r))




if __name__ == "__main__":
    app.run()
