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
        q1 = int(request.form['Q1'])
        q2 = int(request.form['Q2'])
        q3 = int(request.form['Q3'])
        q4 = int(request.form['Q4'])
        q5 = int(request.form['Q5'])
        q6 = int(request.form['Q6'])
        q7 = int(request.form['Q7'])
        q8 = int(request.form["Q8"])
        q9 = int(request.form["Q9"])
        q10 = int(request.form["Q10"])
        q11 = int(request.form["Q11"])
        q12 = int(request.form["Q12"])
        q13 = int(request.form["Q13"])
        q14 = int(request.form["Q14"])
        q15 = int(request.form["Q15"])
        q16 = int(request.form["Q16"])
        q17 = int(request.form["Q17"])
        q18 = int(request.form["Q18"])
        q19 = int(request.form["Q19"])
        q20 = int(request.form["Q20"])
        q21 = int(request.form["Q21"])


        allparams = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21]
        print(allparams)
        array = np.array(allparams)
        output = model.predict([array]).tolist()
        level = output[0]
        print(output[0])
    return (render_template("predict.html",leveloutput = level))
    

if __name__ == '__main__':
    app.run(DEBUG==True)
