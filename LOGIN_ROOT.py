from flask import Flask,request
from flask_cors import CORS


app = Flask(__name__) #here i set environment varible for flask framework web application
CORS(app)
#-----------------------Configuration-------------------
from user import *
    
@app.route("/My_Signup_Details",methods=['POST'])
def My_Signup_Details():
    return User_logup_Details(request)

@app.route("/My_Signin_Details",methods=['POST'])
def My_Signin_Details():
    return User_login_Details(request)

if __name__ == "__main__":
    app.run(host ='192.168.1.2',port =5000)
    #app.run(debug=True)
    
