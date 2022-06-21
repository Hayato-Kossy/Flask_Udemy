from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form

app = Flask(__name__)

app.config["SEACRET_KEY"] = b'\xac\xae:\x0f\x05\x87j\xe85\xac5&m\x9b\xbcG'

class UserForm(Form):
    name = StringField("名前")
    age = IntegerField("年齢")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    name = age = ""
    form = UserForm(request.form)
    if request.method == "POST":
        if form.validate():
            name = form.name.data
            age = form.age.data
            form = UserForm()
        else:
            print("入力内容に問題があります")
    return render_template("index.html", form=form, name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)