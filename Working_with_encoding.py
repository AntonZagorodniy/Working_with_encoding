import json
import chardet
from collections import Counter
from pprint import pprint

def open_file(name):
    text = {}
    try:
        with open(name, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)
            cod = (result['encoding'])
    except FileNotFoundError:
        print('Файл не найден')
    with open(name, encoding=cod) as f:
        data = json.load(f)
        text.update(data)
    return text
    print('Файл не найден')
    # pprint(text)


def parsing_text(open_file):
    text = open_file
    str_words_1 = text['rss']['channel']['items'][0]['description']
    str_words_2 = text['rss']['channel']['items'][0]['title']
    str_words = str_words_1 + str_words_2
    words = str_words.split(' ')
    new_words = []
    for word in words:
        if len(word) > 5:
            new_words.append(word)
        new_words.sort()
    # print(new_words)
    dict_words = (Counter(new_words).items())
    d = list(dict_words)
    d.sort(key=lambda i: i[1])
    d.reverse()
    repeat_words = ""
    for i in range(1, 10):
        repeat_words = repeat_words +", "+ (d[i][0])
    repeat_words = d[0][0] + repeat_words.lstrip()
    return repeat_words

def parsing_text_newsfr():
    repeat_words = parsing_text(open_file_newsfr())
    print("Наиболее употребляемые слова в новостях Кипра:", repeat_words)


def parsing_text_newscy():
    repeat_words = parsing_text(open_file_newscy())
    print("Наиболее употребляемые слова в новостях Кипра из еще одного файла:", repeat_words)


def parsing_text_newsafr():
    repeat_words = parsing_text(open_file_newsafr())
    print("Наиболее употребляемые слова в новостях Африки:", repeat_words)


def parsing_text_newsit():
    repeat_words = parsing_text(open_file_newsit())
    print("Наиболее употребляемые слова в новостях Италии:", repeat_words)


def open_file_newsafr():
    text_newsafr = open_file('newsafr.json')
    return text_newsafr


def open_file_newscy():
    text_newscy = open_file('newscy.json')
    return text_newscy


def open_file_newsfr():
    text_newsfr = open_file('newsfr.json')
    return text_newsfr


def open_file_newsit():
    text_newsfr = open_file('newsit.json')
    return text_newsfr


def Tape_travel_news():
    parsing_text_newsfr()
    parsing_text_newscy()
    parsing_text_newsafr()
    parsing_text_newsit()


Tape_travel_news()
