import pandas as pd
import sqlite3 as db

con = db.connect('chinese.db')

chengyu = pd.read_json('chengyu.json')

def insert(cur, word, pinyin, abbr, ascii_pinyin, explanation, example, derivation):
    cur.execute(
        """
        INSERT INTO Chengyu VALUES(
            NULL,
            '{0}',
            '{1}',
            '{2}',
            '{3}',
            '{4}',
            '{5}',
            '{6}'
        )
        """.format(
            word, pinyin, abbr, ascii_pinyin, explanation, example, derivation
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
        DROP INDEX IF EXISTS ind_abbr
        """
    )
    cur.execute(
        """
        DROP INDEX IF EXISTS ind_pinyin
        """
    )
    cur.execute(
        """
        CREATE TABLE Chengyu(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            abbrev TEXT NOT NULL,
            ascii_pinyin TEXT NOT NULL,
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
    cur.execute(
        """
        CREATE INDEX ind_pinyin on Chengyu (ascii_pinyin)
        """
    )
    for index, row in chengyu.iterrows():
        print(index)
        insert(cur, row["word"], row["pinyin"], row["abbreviation"], row["ascii_pinyin"], row["explanation"], row["example"], row["derivation"])
