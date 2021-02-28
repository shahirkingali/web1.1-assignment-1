from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_desserts>')
def favorite_dessert(users_desserts):
    return f"How did you know I liked {users_desserts}? "


@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f" They were {adjective} across {noun}"


@app.route('/multiply/<number1>/<number2>')
def muliplication(number1, number2):
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f"{number1} times {number2} is {result}"
    else:
        return"Invalid inputs. Please try again by entering 2 numbers!"


@app.route('/sayntimes/<word>/<n>')
def sayntime(word, n):
    number = int(n)
    for w in range(number):
        w = (word + " ") * number
        return f" {w} "


@app.route('/dicegame')
def roll():
    rolled_num = random.randint(1, 6)
    if rolled_num == 6:
        return f" You rolled a {rolled_num}. You won!"
    else:
        return f"You rolled a {rolled_num}. You lost!"


if __name__ == '__main__':
    app.run(debug=True)
