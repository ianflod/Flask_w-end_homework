
from flask import render_template
from app import app
from models.game import who_wins
from models.player import *

@app.route('/')
def index():
    return "Lets play Rock, Paper, Scissors!"



@app.route('/<player1_choice>/<player2_choice>')
def index2(player1_choice, player2_choice):
    p1 = player1_choice
    p2 = player2_choice
    winner = who_wins(player1_choice, player2_choice)
    return render_template('index.html', title='Rock, Paper, Scissors', p1=p1, p2=p2, winner=winner)