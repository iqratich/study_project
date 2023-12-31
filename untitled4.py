# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HZ0dLrdkkNXAnCoJ6wh9i7hUb-GGtjyk
"""

import random

# Функция, проверяющая, является ли слово в списке допустимым
def is_valid_word(word, words_list):
    return word in words_list

def generate_grid(size=10, max_words=None):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            letter = random.choice("abcdefghij")
            row.append(letter)
        grid.append(row)
    if max_words:
        words_list = set()
        while len(words_list) < max_words:
            word = generate_word()
            if is_valid_word(word, words_list):
                words_list.add(word)
        shuffle(words_list)
        print(f"Generated {max_words} valid words to fill the grid:")
        for word in words_list:
            print(word)
    return grid

def display_grid(grid):
    width = len(max(grid, key=len))