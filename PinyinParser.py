map_abbr = {'ā':'a', 'á':'a', 'ǎ':'a', 'à':'a', 'ō':'o', 'ó':'o', 'ǒ':'o', 'ò':'o',\
            'ē':'e', 'é':'e', 'ě':'e', 'è':'e', 'ī':'i', 'í':'i', 'ǐ':'i', 'ì':'i',\
            'ū':'u', 'ú':'u', 'ǔ':'u', 'ù':'u', 'ǖ':'v', 'ǘ':'v', 'ǚ':'v', 'ǜ':'v', 'ü':'v'}
map_tone = {'ā':1, 'á':2, 'ǎ':3, 'à':4, 'ō':1, 'ó':2, 'ǒ':3, 'ò':4,\
           'ē':1, 'é':2, 'ě':3, 'è':4, 'ī':1, 'í':2, 'ǐ':3, 'ì':4,\
            'ū':1, 'ú':2, 'ǔ':3, 'ù':4, 'ǖ':1, 'ǘ':2, 'ǚ':3, 'ǜ':4}
def asciiOf(pinyin):
    each = list(pinyin)
    return ''.join(list(map(lambda x: map_abbr[x[:1]] if x[:1] in map_abbr else x[:1], each)))
def tone(pinyin):
    each = list(pinyin)
    return max(list(map(lambda x: map_tone[x[:1]] if x[:1] in map_tone else 0, each)))
