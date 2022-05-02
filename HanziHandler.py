import pandas as pd
from PinyinParser import *

chengyu = pd.read_json('hanzi.json')

chengyu['abbreviation'] = chengyu['pinyin'].apply(asciiOf)
chengyu['tone'] = chengyu['pinyin'].apply(tone)

chengyu.to_json('hanzi.json', force_ascii=False, orient='records')