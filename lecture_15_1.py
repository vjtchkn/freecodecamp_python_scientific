# Creating a database table
import sqlite3

conn = sqlite3.connect("music.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Tracks")
cur.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")

# Inserting data
cur.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("Thunderstruck", 20))
cur.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("My Way", 15))
conn.commit()

# Access data
print("Tracks:")
cur.execute("SELECT title, plays FROM Tracks")
for row in cur:
    print(row)

# Delete data
cur.execute("DELETE FROM Tracks WHERE plays < 100")
conn.commit()

conn.close()
