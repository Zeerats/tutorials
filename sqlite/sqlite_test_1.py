import sqlite3


# Links to the database. Can either be a file or an in RAM database, which will start from scratch each time the code is executed.
conn = sqlite3.connect(':memory:') # Use ':memory:' for testing. Otherwise, link to database (.db) file.

# Creates a cursor to run queries/commands on the database.
c = conn.cursor()

# Creates a table with three columns specifying their data types.
c.execute("CREATE TABLE players (name text, race text, level integer)")

# Inserts a player into the database with an ID and level.
c.execute("INSERT INTO players VALUES ('TheLegend', 'Elf', 100)")
c.execute("INSERT INTO players VALUES ('NoobMike', 'Orc', 23)")

# Selects all players with level 100.
c.execute("SELECT * FROM players WHERE level=100")

print(c.fetchall())

### c.fetchone() # Gets the first row of the results of the query.
### c.fetchmany(5) # Will get five (or any number passed) rows of recults of the query.
### c.fetchall() # Will return all results of the query.

conn.commit() # Commits the changes to the database.
conn.close() # Closes the connection to the database.
