# HanziDictData

A prefilled sqlite database file for hanzi

Data comes from [pwxcoo/chinese-xinhua](https://github.com/pwxcoo/chinese-xinhua)

## What is included in this repo

1. Prefilled sqlite database file
    - Table hanzi: 字典
    - Table ciyu：词典
    - Table chengyu：成语词典
    - Table xiehouyu：歇后语
2. Python scripts I import data from json to database
    - `PinyinParser.py`: split `pinyin` into `abbrev`(不含声调的拼音) and `tone`(声调)
    - `*_to_db.py`: fill data into database
