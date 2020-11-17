import sqlite3
from player_test import Player # Imports the example class from 'player_test.py'.


# Links to the database. Can either be a file or an in RAM database, which will start from scratch each time the code is executed.
conn = sqlite3.connect(':memory:') # Use ':memory:' for testing. Otherwise, link to database (.db) file.

# Creates a cursor to run queries/commands on the database.
c = conn.cursor()

# Creates instances of the player class. Attributes are name, race and level.
player_1 = Player('TheLegend', 'Elf', 100)
player_2 = Player('NoobMike', 'Orc', 27)

# Creates a table with three columns specifying their data types.
c.execute("CREATE TABLE players (name text, race text, level integer)")

# Inserts a player into the database using placeholders to reference the atributes from the players instances.
c.execute("INSERT INTO players VALUES (:name, :race, :level)", {'name': player_1.name, 'race': player_1.race, 'level': player_1.level})
c.execute("INSERT INTO players VALUES (:name, :race, :level)", {'name': player_2.name, 'race': player_2.race, 'level': player_2.level})

# Selects players passing different levels to the query.
c.execute("SELECT * FROM players WHERE level=100 OR level=27")

print(c.fetchall())

conn.commit() # Commits the changes to the database.
conn.close() # Closes the connection to the database.
