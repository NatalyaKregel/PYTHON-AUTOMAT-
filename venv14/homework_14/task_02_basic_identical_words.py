'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых 
частых. Не учитывать знаки препинания и регистр символов.
'''
import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """сегодня сегодня солнце изморозь изморозь изморозь"""
print(top_10_words(text))