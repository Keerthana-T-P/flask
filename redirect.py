'''from flask import Flask, redirect
app = Flask(__name__)
@app.route("/")
def home():
    return redirect("/helloworld")

@app.route("/helloworld")
def hello_world():
    return "<p>Hello, World from redirected page.!</p>"
  
 
if __name__ == '__main__':
    app.run(debug=True)'''
from flask import Flask, abort, redirect, url_for, render_template, request

# Initialize the flask application 
app = Flask(__name__)

# This route will load the form template which is in login.html
@app.route('/')
def load_login():
    return render_template("login.html")

@app.route('/success')
def success():
    return "Logged in successfully"

# Logging to the form with method POST or GET 
@app.route("/login", methods=["POST", "GET"])
def login():
    # If the method is POST and Username is admin, then it redirects to success url
    if request.method == "POST" and request.form["username"] == "admin":
        return redirect(url_for("success"))

    # If the method is GET or username is not admin, then it redirects to index method
    return redirect(url_for('load_login'))

@app.route('/<uname>')
def check_username(uname):
    if uname[0].isdigit():
        abort(403)
    return '<h1>Good Username</h1>'

if __name__ == '__main__':
    app.run(debug=True)
'''change host
set FLASK_APP=app.py
flask run
flask run --host=192.168.0.105 --port=5000'''