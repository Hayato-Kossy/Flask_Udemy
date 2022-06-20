from flask import Flask, render_template, redirect, url_for, abort
from datetime import datetime
app = Flask(__name__, template_folder="templates")

@app.template_filter("born_year")
def calcurate_born_year(age):
    now_timestanmp = datetime.now()
    return str(now_timestanmp.year - int(age)) + '年'

@app.template_filter("reverse_name")
def reverse(name):
    return name[-1::-1]

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/home/<string:user_name>/<int:age>")
def home(user_name, age):
    user_info = {
        "name" : user_name,
        "age"  : age,
    }
    return render_template("home.html", user_info=user_info)

class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route("/userlist")
def user_list():
    users = [
        UserInfo("Taro", 21), UserInfo("Jiro", 32), UserInfo("Hanako", 31)
    ]
    is_login = False
    return render_template("userlist.html", users=users, is_login=is_login)
@app.route("/user/<string:user_name>/<int:age>")
def user(user_name, age):
    if user_name in ["Taro", "Jiro", "Saburo"]:
        return redirect(url_for("home", user_name=user_name, age=age))
    else:
        abort(500, "そのユーザはリダイレクトできません")
@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template("system_error.html", error_description=error_description), 500
     
@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html"), 404

if __name__ == "__main__":
    app.run(debug=True)