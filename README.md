# UAI-home-questions(web)
 UAI-home-questions(web)

Для создания веб-приложения на Flask с лотереей необходимо выполнить следующие шаги:

1. Установить Flask:

```
pip install flask
```

2. Создать файл app.py и добавить следующий код:

```python
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
```

3. Создать папку templates и создать там файлы index.html, players.html, game.html и winner.html со следующим содержимым:

index.html:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Lottery Game</title>
</head>
<body>
	<h1>Welcome to the Lottery Game!</h1>
	<p>Here are the <a href="/players">players</a> and the <a href="/game">game</a> rules:</p>
	<ul>
		<li>There can be between 2 and 10 players.</li>
		<li>Each player will be assigned a random number between 0 and 100.</li>
		<li>The player with the highest number wins.</li>
		<li>In case of a tie, nobody wins.</li>
	</ul>
</body>
</html>
```

players.html:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Lottery Game - Players</title>
</head>
<body>
	<h1>Players:</h1>
	<ul>
		{% for player in players %}
			<li>{{ player }}</li>
		{% endfor %}
	</ul>
	<form action="/add_player" method="post">
		<label for="name">Add yourself as a player:</label>
		<input type="text" id="name" name="name">
		<button type="submit">Add</button>
	</form>
</body>
</html>
```

game.html:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Lottery Game - Game</title>
</head>
<body>
	<h1>The game is on!</h1>
	<p>Here are the results:</p>
	<ul>
		{% for player, result in results.items() %}
			<li>{{ player }}: {{ result }}</li>
		{% endfor %}
	</ul>
	<form action="/winner">
		<button type="submit">And the winner is...</button>
	</form>
</body>
</html>
```

winner.html:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Lottery Game - Winner</title>
</head>
<body>
	<h1>The winner is...</h1>
	<p>{{ winner }}</p>
	<p><a href="/">Play again?</a></p>
</body>
</html>
```

4. Запустить приложение:

```
python app.py
```

5. Открыть браузер и перейти на http://localhost:5000/ для начала игры.

Готово! Теперь вы можете играть в лотерею с вашими друзьями.