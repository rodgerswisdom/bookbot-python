#!/usr/bin/env python3

def count(FILE_PATH):
    with open(FILE_PATH, "r") as file:
        content = file.read()
        num_words = len(content.split())

        text = content.lower()
        word_dict = {}

        for char in text:
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1

        return word_dict


def count_list(word_dict):
    str_list = [{"key":key,"value":value} for key,value in word_dict.items()]
    str_list = sorted(str_list, key=lambda x:x["value"], reverse=True)
    return str_list

