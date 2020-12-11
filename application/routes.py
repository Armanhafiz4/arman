from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all() #all selects all from games and first only selects 1
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>') #whatever we change name to will be our game name
def update(name):
    first_game = Games.query.first() #only shows the first/latest game added in read file
    first_game.name = name
    db.session.commit() #for an update you dont need to add so just commit as its already in the db
    return first_game.name

@app.route('/delete')
def delete():
    first_game = Games.query.first()
    db.session.delete(first_game)
    db.session.commit()
    return "Deleted the first game"

@app.route('/count')
def count():
    number_of_games = Games.query.count()
    return f"There are {number_of_games} games in this database"