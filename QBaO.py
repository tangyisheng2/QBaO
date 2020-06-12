#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   QBaO.py.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2020, Tang Yisheng

@Modify Time        @Author     @Version        @Desciption
------------        -------     --------        -----------
2020/6/12 10:53     Tang        1.0             None
"""

import os
import random
import json
import jieba.posseg

DEFAULT_P = 0.9
suffix_words = ['个屁', '个头', '个几把', '个鬼', '个卵']
character_replacement_data = dict()


def generate_repeat_text(text):
    output = ''
    for char in text:
        replacement = character_replacement_data.get(char)
        output += replacement if replacement else char
    return output


def generate_insult_text(text):
    suffix_word = random.choice(suffix_words)
    keywords = list()
    input_words = jieba.posseg.cut(text)
    for w in input_words:
        if w.flag.startswith('v') or w.flag.startswith('a') or w.flag == 'i':
            keywords.append(w.word)
    if keywords:
        return random.choice(keywords) + suffix_word
    return None


def load_char_replace_data():
    global character_replacement_data
    if os.path.isfile('char_replace_data.json'):
        with open('char_replace_data.json') as f:
            character_replacement_data = json.load(f)
    else:
        print('ERROR: char_replace_data.json does not exist')


def main():
    load_char_replace_data()
    print("你好，我是练习时长两年半的Q宝，一起来聊天吧！")
    while True:
        output = ''
        text = input("我：")
        if random.randint(0, 10) < DEFAULT_P * 10:
            if random.randint(0, 10) > 5:
                output = generate_insult_text(text)
            elif random.randint(0, 10) <= 5:
                output = generate_repeat_text(text)
            print(output)
        else:
            print("你说啥我没听清~")

    pass


if __name__ == '__main__':
    main()
