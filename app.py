from re import DEBUG
import numpy as np
from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def hello_world():
     return render_template('main.html')

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/predict",methods=['GET','POST'])

def prediction():
    if(request.method == 'POST'):
        nervousness = int(request.form['Q1'])
        control = int(request.form['Q2'])
        Worry = int(request.form['Q3'])
        relaxation = int(request.form['Q4'])
        restlessness = int(request.form['Q5'])
        irritable = int(request.form['Q6'])
        fear = int(request.form['Q7'])
        name = request.form["name"]
        allparams = [nervousness,control,Worry,relaxation,restlessness,irritable,fear]
        print(allparams)
        array = np.array(allparams)
        output = model.predict([array]).tolist()
        level = output[0]
       
        print(output)
    return (render_template("predict.html",output = level,name = name ))
    

if __name__ == '__main__':
    app.run(DEBUG==True)
