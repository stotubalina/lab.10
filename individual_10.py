#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"b", "d", "j", "n", "t", "v"}
    b = {"f", "g", "j", "r", "t", "x"}
    c = {"o", "p", "x"}
    d = {"a", "f", "m", "s", "x", "y"}
    x = (a.intersection(b)).union(c)
    print(f"x = {x}")
    an = u.difference(a)
    y = (an.intersection(d)).union(c.difference(b))
    print(f"y = {y}")
    