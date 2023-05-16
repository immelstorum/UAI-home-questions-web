from flask import Flask, render_template, request
import random

app = Flask(__name__)

players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]
results = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def player_list():
    return render_template('players.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.form['name']
    players.append(name)
    return render_template('players.html', players=players)

@app.route('/game')
def game():
    global results
    results = {}
    for player in players:
        results[player] = random.randint(0, 100)
    return render_template('game.html', results=results)

@app.route('/winner')
def winner():
    global results
    winner = max(results, key=results.get)
    count = list(results.values()).count(results[winner])
    if count > 1:
        return render_template('winner.html', winner="Nobody (tie)")
    else:
        return render_template('winner.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)