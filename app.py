import pickle
from flask import Flask,request


model1=pickle.load(open('model1.pkl','rb'))  

app=Flask(__name__)

#handler
@app.route('/')
def homepage():
    return 'API Server Launched'


@app.route('/predict',methods=['GET'])
def predict():
    age=float(request.args.get('age'))
    sex=float(request.args.get('sex'))
    cp=float(request.args.get('cp'))
    trtbps=float(request.args.get('trtbps'))
    chol=float(request.args.get('chol'))
    fbs=float(request.args.get('fbs'))
    resteg=float(request.args.get('resteg'))
    thalac=float(request.args.get('thalac'))
    Exng=float(request.args.get('Exng'))
    slp=float(request.args.get('slp'))
    oldpeak=float(request.args.get('oldpeak'))
    thall=float(request.args.get('thall'))
    caa=float(request.args.get('caa'))
    data=[[age,sex,cp,trtbps,chol,fbs,resteg,thalac,Exng,slp,oldpeak,thall,caa]]
    result=model1.predict(data)[0]
    return result

if __name__=="__main__" :
    app.run(
        host='0.0.0.0',  #for local host='127.0.0.0'
        port=5000,
        debug=True
    )