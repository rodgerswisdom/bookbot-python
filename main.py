#!/usr/bin/env python3

from stats import *

def main():
    FILE_PATH = "books/frankeinstein.txt"

    text = count(FILE_PATH)
    word_count = len(text)
    count_text = count_list(text)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for items in count_text:
        if items["key"].isalpha():
            print(f"{items["key"]}:{items["value"]}")

if __name__ ==  "__main__":
    main()
