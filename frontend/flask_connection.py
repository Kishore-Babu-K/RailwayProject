from flask import Flask , render_template, url_for, redirect, request, flash,get_flashed_messages
from UserDao import login_check , Register_new
from TrainDao import Search_train_by_station , Search_train_by_name
from sqlconnection import make_sql_connection


connection = make_sql_connection()
app = Flask(__name__)
app.secret_key = "I Have No Enemies"


@app.route("/login",methods = ["POST","GET"])
def logincheck():
    userid = request.form.get("user_id")
    password = request.form.get("pass_word")
    data = {
        "user_id" : userid,
        "pass_word" : password
    }
    checkpass = login_check(connection,data)
    if checkpass:
        return render_template("userhome.html")
    else:
        return flash("Invalid Login Credentials","error")



@app.route("/signup",methods = ["POST"])
def signup():
    userid = request.form.get("user_id")
    username = request.form.get("user_name")
    password = request.form.get("pass_word")
    role = request.form.get("role_of_user")
    phone = request.form.get("phone_num")
    email = request.form.get("email")

    data = {
        "user_id" : userid,
        "user_name" : username,
        "pass_word" : password,
        "role_of_user" : role,
        "phone_num" : phone,
        "email" : email
    }

    Register_new(connection,data)
    return render_template("loginpage.html")

@app.route("/searchtrain", methods = ["POST","GET"])
def search_train_station():
  trainsinfo = []
  if request.method == "POST":  
    s_from = request.form.get("from")
    s_to = request.form.get("to")
    
    data = {
        "from" : s_from,
        "to" : s_to
    }

    trainsinfo = Search_train_by_station(connection,data)
    no_train = len(trainsinfo) == 0

    return render_template("searchtrain.html",trainsinfo = trainsinfo, no_train = no_train)

@app.route("/searchname", methods = ["POST","GET"])
def search_train_name():
  trainsinfo = []
  if request.method == "POST":  
    search = request.form.get("train_name")

    data = {
        "search" : search,
    }

    trainsinfo = Search_train_by_name(connection,data)
    no_train = len(trainsinfo) == 0

    return render_template("searchtrain.html",trainsinfo = trainsinfo, no_train = no_train)


#Template Renderers

@app.route("/")
def loginpage():
    return render_template("loginpage.html")

@app.route("/register")
def register():
    return render_template("registerpage.html")

@app.route("/logout")
def logout():
    return render_template("loginpage.html")

@app.route("/homepage")
def homepage():
    return render_template("userhome.html")

@app.route("/search")
def search():
    return render_template("searchtrain.html")


    
if __name__ == "__main__":

    app.run(debug=True)


