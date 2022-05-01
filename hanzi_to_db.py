import pandas as pd
import sqlite3 as db

con = db.connect('chinese.db')

hanzi = pd.read_json('hanzi.json')

def insert(cur, word, pinyin, abbr, tone, strokes, radicals, oldword, explanation, more):
    cur.execute(
        """
        INSERT INTO Hanzi VALUES(
            NULL,
            '{0}',
            '{1}',
            '{2}',
            '{3}',
            '{4}',
            '{5}',
            '{6}',
            '{7}',
            '{8}'
        )
        """.format(
            word, pinyin, abbr, tone, strokes, radicals, oldword, explanation, more
        )
    )

with con:
    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS Hanzi
        """
    )
    cur.execute(
        """
        DROP INDEX IF EXISTS ind_full_pinyin
        """
    )
    cur.execute(
        """
        CREATE TABLE Hanzi(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "character" TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            abbrev TEXT NOT NULL,
            tone INTEGER NOT NULL,
            strokes INTEGER NOT NULL,
            radicals TEXT NOT NULL,
            old_char TEXT NOT NULL,
            explanation TEXT,
            "more" TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE INDEX ind_full_pinyin on Hanzi (abbrev)
        """
    )
    for index, row in hanzi.iterrows():
        print(index)
        insert(cur, row["word"], row["pinyin"], row["abbreviation"], row["tone"], row["strokes"], row["radicals"], row["oldword"], row["explanation"], row["more"])
