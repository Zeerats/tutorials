import sqlite3
from player_test import Player # Imports the example class from 'player_test.py'.


# Links to the database. Can either be a file or an in RAM database, which will start from scratch each time the code is executed.
conn = sqlite3.connect(':memory:') # Use ':memory:' for testing. Otherwise, link to database (.db) file.

# Creates a cursor to run queries/commands on the database.
c = conn.cursor()

# Creates a table with three columns specifying their data types.
c.execute("CREATE TABLE players (name text, race text, level integer)")

# Inserts a player into the database.
def insert_player(player):
    with conn: # Creates a context manager so changes don't need to be committed.
        c.execute("INSERT INTO players VALUES (:name, :race, :level)", {'name': player.name, 'race': player.race, 'level': player.level})


# Returns a player by passing the race to the function.
def get_players_by_race(race):
    c.execute("SELECT * FROM players WHERE race=:race", {'race': race}) # Doesn't need to be within a context manager, as no changes are going to be made to the database.
    return c.fetchall()


# Updates the level of a player.
def update_level(player, level):
    with conn:
        c.execute("""UPDATE players SET level=:level
                    WHERE name=:name AND race=:race""",
                    {'name': player.name, 'race': player.race, 'level': level})


# Removes a player from the database.
def remove_player(player):
    with conn:
        c.execute("DELETE FROM players WHERE name=:name AND race=:race",
                    {'name': player.name, 'race': player.race})


# Creates instances of the player class. Attributes are name, race and level.
player_1 = Player('TheLegend', 'Elf', 100)
player_2 = Player('NoobMike', 'Orc', 27)
player_3 = Player('LegolasTheElf', 'Elf', 42)


### SOME TESTS:
insert_player(player_1) # Insterts the players.
insert_player(player_2)
insert_player(player_3)

elves = get_players_by_race('Elf') # Gets all elves.
print(elves)

update_level(player_2, 50) # Updates NoobMike's level to 50.

remove_player(player_3) # Removes LegolasTheElf from the database.

orcs = get_players_by_race('Orc') # Gets all orcs.
print(orcs)

elves = get_players_by_race('Elf') # Gets all elves to check that LegolasTheElf has been removed.
print(elves)

conn.close() # Closes the connection to the database.
