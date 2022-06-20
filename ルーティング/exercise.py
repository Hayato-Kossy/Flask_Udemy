from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def Q1():
    return "<h1>こんにちは</h1>"

@app.route("/hello/<string:username1>/<string:username2>")
def Q2(username1, username2):
    return "<h1>こんにちは{}さん、{}さん</h1>".format(username1, username2)

@app.route("/hello/<int:num1>/<int:num2>")
def Q3(num1, num2):
    sum_num = str(num1 + num2)
    return "<h1>{}</h1>".format(sum_num)
   

if __name__ == "__main__":
    app.run(debug=True)