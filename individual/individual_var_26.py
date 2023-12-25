#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо определить результат выполнения операции над множествами.

if __name__ == "__main__":
    a = {'a', 'b', 'c', 'd', 'e', 'r'}
    b = {'b', 'c', 'd', 'f', 'n', 'y'}
    c = {'b', 'c', 'h', 'k', 'l', 's'}
    d = {'a', 'b', 'r', 's', 'w', 'x'}

    # Так как в выражении есть логическое 'не', то нужно создать универсум.
    u = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    # Запишем решение данных операций над множествами.
    x = (a.union(d)).intersection(c)
    y = (a.difference(d)).union((u.difference(c)).difference(u.difference(b)))
    print("X = \n", x)
    print("Y = \n", y)
