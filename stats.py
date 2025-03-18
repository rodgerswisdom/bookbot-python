#!/usr/bin/env python3

def count(FILE_PATH):
    with open(FILE_PATH, "r") as file:
        content = file.read()
        num_words = len(content.split())
        print(f"{num_words} words")


