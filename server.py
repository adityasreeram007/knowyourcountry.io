from flask import Flask,render_template,request,make_response,redirect
import json
import requests
app = Flask(__name__)
@app.route("/",methods=['GET'])
def query():

    data=requests.get("https://restcountries.com/v3.1/all",timeout=1.0)
    res=data.json()
    print(res[0])
    return render_template('homepage.html',arr=res)

if __name__ == "__main__":
    app.run(port=5008,debug=True)
