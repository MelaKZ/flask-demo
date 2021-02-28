from flask import Flask, render_template, request, session
import datetime
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Nazgulz rock!"
    return render_template("index.html", headline=headline)


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "You should submit the post to get here"
    else:
        name = request.form.get("name")
        return render_template("hello.html", jname=name)


@app.route("/more")
def more():
    return render_template("more.html")


notes_list = []

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        note = request.form.get("note")
        notes_list.append(note)
    return render_template("notes.html", notes=notes_list)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/session_notes_", methods=["GET", "POST"])
def session_notes_():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("session_notes_.html", notes=session["notes"])


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
def valami(shhhh):
    return f"Hello, {shhhh}!"
