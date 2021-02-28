from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Nazgulz rock!"
    return render_template("index.html", headline=headline)


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name_")
    return render_template("hello.html", jname=name)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/names")
def forloop():
    names = ["Alice", "Józsibácsi", "Nazgul"]
    return render_template("forloop.html", names=names)


@app.route("/new")
def n_y():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    return render_template("newyear.html", new_year=new_year, date_=str(now))


@app.route("/KZ")
def zottya():
    return "<h1>Hello, MelaKZ!!!</h1>"


@app.route("/<string:name>")
def hello(shhhh):
    return f"Hello, {shhhh}!"
