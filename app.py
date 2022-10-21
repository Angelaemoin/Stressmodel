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
# q1 = request.args['Q1']
# def predict():
#    return render_template("predict.html",output=q1)
def prediction():
    if(request.method == 'POST'):
        q1 = int(request.form['Q1'])
        q2 = int(request.form['Q2'])
        q3 = int(request.form['Q3'])
        q4 = int(request.form['Q4'])
        q5 = int(request.form['Q5'])
        q6 = int(request.form['Q6'])
        q7 = int(request.form['Q7'])
        allparams = [q1,q2,q3,q4,q5,q6,q7]
        print(allparams)
        array = np.array(allparams)
        output = model.predict([array]).tolist()
        print(output)


       
    # return (model.predict([[3,3,3,3,3,3,3]]).tolist())
    return (render_template("predict.html",output = output) )
    

if __name__ == '__main__':
    app.run(debug==True)
