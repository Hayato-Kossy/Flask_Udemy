from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"
    
@app.route("/user/<string:user_name>/<int:user_no>")
def show_user(user_name, user_no):
    user_name_no = user_name + str(user_no)
    return "<h1>{}</h1>".format(user_name_no)

if __name__ == "__main__":
    app.run(debug=True)