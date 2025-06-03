from flask import Flask, render_template, request, redirect, url_for
from database import add_user, getuser, save_workout
from workout_generator import generate_workout
from chat_agent import chat_with_ai



app = Flask(__name__)


# In-memory chat history (just for demo)
chat_memory = []


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        fitness_level = request.form["fitness_level"]
        goal = request.form["goal"]
        equipment = request.form["equipment"]


        add_user(name, age, fitness_level, goal, equipment)
        return redirect(url_for("workout", username=name))
    return render_template("register.html")



@app.route("/workout", methods=["GET", "POST"])
def workout():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("result", username=username))
    return render_template("workout.html")



@app.route("/workout/result/<username>")
def result(username):
    user = get_user(username)
    if not user:
        return f"User '{username}' not found.", 404
    
