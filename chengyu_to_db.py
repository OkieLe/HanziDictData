import pandas as pd
import sqlite3 as db
 
con = db.connect('chinese.db')

chengyu = pd.read_json('chengyu.json')

def insert(cur, word, pinyin, abbr, explanation, example, derivation):
    cur.execute(
        """
        INSERT INTO Chengyu VALUES(
            NULL,
            '{0}',
            '{1}',
            '{2}',
            '{3}',
            '{4}',
            '{5}'
        )
        """.format(
            word, pinyin, abbr, explanation, example, derivation
        )
    )
 
 
with con:
    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS Chengyu
        """
    )
    cur.execute(
        """
        CREATE TABLE Chengyu(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            abbrev TEXT NOT NULL,
            explanation TEXT,
            example TEXT,
            derivation TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE INDEX ind_abbr on Chengyu (abbrev)
        """
    )
    for index, row in chengyu.iterrows():
        print(index)
        insert(cur, row["word"], row["pinyin"], row["abbreviation"], row["explanation"], row["example"], row["derivation"])
