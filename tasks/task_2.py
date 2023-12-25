#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо решить задачу: необходимо определить общие
# символы в двух строках, введенных с клавиатуры.

if __name__ == "__main__":
    first_sentence = input("Введите первое продложение: ")
    second_sentence = input("Введите второе предложение: ")
    symbols = set(second_sentence).intersection(set(first_sentence))
    print("Общие символы находящиеся в обоих предложениях: \n", ','.join(symbols))
