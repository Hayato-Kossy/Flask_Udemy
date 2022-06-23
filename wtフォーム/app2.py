from flask import (
    Flask, render_template, request, session, redirect, url_for
)
from wtforms import Form
from wtforms import (
    StringField, IntegerField, BooleanField, DateField, PasswordField,
    RadioField, SelectField, TextAreaField, SubmitField
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "mykey"

class UserForm(Form):
    name = StringField("名前：　")
    age = IntegerField("年齢：　")
    password = PasswordField("パスワード：　")
    birthday = DateField("誕生日：　", format="%Y/%m/%d")
    gender = RadioField("性別：　", choices=[("man", "男性"), ("woman", "女性")])
    major = SelectField("専攻：　", choices=[("bungaku", "文学部"), ("hougaku", "法学部"), ("rigaku", "理学部")])
    is_japanese = BooleanField("日本人？：　")
    message = TextAreaField("メッセージ：　")
    submit = SubmitField("送信")

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        session["name"] = form.name.data
        session["age"] = form.age.data
        session["birthday"] = form.birthday.data
        session["gender"] = form.gender.data
        session["major"] = form.major.data
        session["nationality"] = "日本人" if form.is_japanese.data else "外国人"
        session["message"] = form.message.data
        return redirect(url_for("show_user"))
    return render_template("user_regist.html", form=form)

@app.route("/show_user")
def show_user():
    return render_template("show_user.html")

if __name__ == "__main__":
    app.run(debug=True)