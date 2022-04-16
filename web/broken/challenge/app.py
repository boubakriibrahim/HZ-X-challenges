
from flask import Flask
from flask import render_template , request
import pandas as pd
from csv import writer
import random

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "message" : "server is running"
    }

@app.route("/profile")
def profile():
    return render_template("index.html")

@app.route("/login" , methods = ['post', 'get'])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    elif request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")

        users = pd.read_csv("./ressources/users.csv", delimiter=',')
        auth_user = users.loc[(users["username"] == username) & (users["password"] == password)]
        if (auth_user["role"] == "root").any() :
            f = open("./ressources/flag.txt")
            msg = f.readline()
            f.close()
            return {
                "flag" : msg
            }

        return {
            "response" : auth_user[["user_id","role"]].to_dict("records")
        }

@app.route("/subscribe" , methods = ['post' , 'get'])
def subscribe():
    if request.method == "GET":
        return render_template("subscribe.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")
        if role == None :
            role = "user"
        user_id = random.randint(0,999999)

        with open("./ressources/users.csv" , 'a', newline='') as f_object :
            writer_object = writer(f_object)
            writer_object.writerow([user_id,role,username,password])
            f_object.close()

        return {
            "username" : username,
            "password" : password,
            "role" : role
        }

    