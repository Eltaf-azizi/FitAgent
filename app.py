from flask import Flask, render_template, request, redirect, url_for
from database import add_user, getuser, save_workout
from workout_generator import generate_workout
from chat_agent import chat_with_ai



app = Flask(__name__)


# In-memory chat history (just for demo)
chat_memory = []