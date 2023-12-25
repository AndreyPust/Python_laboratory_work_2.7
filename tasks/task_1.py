#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо решить задачу: посчитать количество гласных в строке, введенной
# с клавиатуры с использованием множеств.

if __name__ == "__main__":
    letters_gl = {'о', 'е', 'ё', 'а', 'и', 'у', 'я', 'ы', 'ю', 'я'}
    words = input("Введите предложение: ")
    print("Количество гласных букв в этом предложении: ")
    count = 0
    for letter in words.lower():
        if letter in letters_gl:
            count += 1
    print(count)
