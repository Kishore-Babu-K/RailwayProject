from flask import Flask , render_template, url_for, redirect, request, flash,get_flashed_messages
from UserDao import login_check , Register_new
from TrainDao import Search_train_by_station , Search_train_by_name, Train_schedule_by_name,Train_schedule_by_no
from TicketDao import Check_Avl_Price_Name, Check_Avl_Price_No
from sqlconnection import make_sql_connection
from ast import literal_eval


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
        flash("Login Success","success")
        return redirect(url_for('homepage'))
    else:
        flash("Invalid Login Credentials","danger")
        return render_template("loginpage.html")



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

@app.route("/trainschedule", methods=["POST", "GET"])
def train_schedule():
    scheduleinfo = None
    if request.method == "POST":

        train_no = request.form.get("train_no")
        train_name = request.form.get("train_name")

        if train_no:
            data = {"train_no": train_no}
            scheduleinfo = Train_schedule_by_no(connection, data)
        elif train_name:
            data = {"train_name": train_name}
            scheduleinfo = Train_schedule_by_name(connection, data)

        no_train = len(scheduleinfo) == 0   
        if no_train:
            scheduledata = None
        else:
            trainno = scheduleinfo[0]
            trainname = scheduleinfo[1]
            route = literal_eval(scheduleinfo[2])
            running = literal_eval(scheduleinfo[3])

            scheduledata = {
                "train_no": trainno,
                "train_name": trainname,
                "route": ' -> '.join(route),
                "running_date": " | ".join(running) 
            }
        print(scheduledata)
        return render_template("trainschedule.html", scheduledata=scheduledata, no_train=no_train)


@app.route("/check_avl_name", methods = ["POST","GET"])
def check_avl_name():
    avlinfo = None
    if request.method == "POST":

        train_no = request.form.get("train_no")
        train_name = request.form.get("train_name")

        if train_no:
            data = {"train_no": train_no}
            avlinfo = Check_Avl_Price_No(connection, data)
        elif train_name:
            data = {"train_name": train_name}
            avlinfo = Check_Avl_Price_Name(connection, data)

        no_train = len(avlinfo) == 0
        print(avlinfo)
        return render_template("checkticket.html", avlinfo=avlinfo, no_train=no_train)


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

@app.route("/schedule")
def schedule():
    return render_template("trainschedule1.html")

@app.route("/checkticket")
def checkticket():
    return render_template("checkticket.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":

    app.run(debug=True)

