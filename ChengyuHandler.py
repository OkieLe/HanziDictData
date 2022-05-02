import pandas as pd
from PinyinParser import *

chengyu = pd.read_json('chengyu.json')

def asciiOfChengyu(pinyin):
    each = pinyin.replace("，", " ").split()
    return ''.join(list(map(asciiOf, each)))

chengyu['ascii_pinyin'] = chengyu['pinyin'].apply(asciiOfChengyu)

chengyu.to_json('chengyu.json', force_ascii=False, orient='records')