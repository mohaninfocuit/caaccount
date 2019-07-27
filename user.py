from sqlwrapper import *
import json

def User_logup_Details(request):
    d = request.json
    print(d)
    d1= gensql('insert','user_login',d)
    return json.dumps({"Return": "Signup Successfully","ReturnCode": "SS","Status": "Success","StatusCode": "200"},indent = 4)

def User_login_Details(request):
    d = request.json
    check_item = json.loads(dbget("select count(*) from user_login \
                                     where username='"+str(d['username'])+"' and password= '"+str(d['password'].title())+"'"))
    if check_item[0]['count'] ==1:
        return json.dumps({"Return": "Login Successfully","ReturnCode": "RS","Status": "Success","StatusCode": "200"},indent = 4)
    else:
        return json.dumps({"Return": "Please Enter Valid Username","ReturnCode": "PEVU","Status": "Success","StatusCode": "200"},indent = 4)
    
    
