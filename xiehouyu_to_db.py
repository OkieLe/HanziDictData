import pandas as pd
import sqlite3 as db

con = db.connect('chinese.db')

xiehouyu = pd.read_json('xiehouyu.json')

def insert(cur, riddle, answer):
    cur.execute(
        """
        INSERT INTO Xiehouyu VALUES(
            NULL,
            '{0}',
            '{1}'
        )
        """.format(
            riddle, answer
        )
    )
with con:
    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS Xiehouyu
        """
    )
    cur.execute(
        """
        CREATE TABLE Xiehouyu(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            riddle TEXT NOT NULL,
            answer TEXT NOT NULL
        )
        """
    )
    for index, row in xiehouyu.iterrows():
        print(index)
        insert(cur, row["riddle"], row["answer"])
