import pandas as pd
import sqlite3 as db

con = db.connect('chinese.db')

ciyu = pd.read_json('ciyu.json')

def insert(cur, word, explanation):
    cur.execute(
        """
        INSERT INTO Ciyu VALUES(
            NULL,
            '{0}',
            '{1}'
        )
        """.format(
            word, explanation
        )
    )

with con:
    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS Ciyu
        """
    )
    cur.execute(
        """
        CREATE TABLE Ciyu(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            explanation TEXT NOT NULL
        )
        """
    )
    for index, row in ciyu.iterrows():
        print(index)
        insert(cur, row["ci"], row["explanation"])
