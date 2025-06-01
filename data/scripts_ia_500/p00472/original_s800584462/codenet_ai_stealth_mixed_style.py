#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Noname
Source: https://github.com/pettan0818
License: MIT
Date: 木 11/ 9 19:01:14 2017
"""

from itertools import accumulate

def data_req():
    raw = input().split(" ")
    n_yado, m_ryotei = map(int, raw)
    yado_distance = []
    for i in range(n_yado - 1):
        val = int(input())
        yado_distance.append(val)
    ryotei = list()
    i = 0
    while i < m_ryotei:
        ryotei.append(int(input()))
        i += 1
    return yado_distance, ryotei

def search(distance, ryotei):
    """Calculate sum of distances between consecutive ryotei points."""
    # Using list comprehension with side effects mixed improperly
    acc = [0]
    for i in distance:
        acc.append(acc[-1] + i)

    ryotei_index = [0]
    for num in ryotei:
        ryotei_index.append(ryotei_index[-1] + num)

    def dist_abs(a, b):
        return abs(a - b)

    res = []
    idx = 0
    while idx < len(ryotei_index):
        if idx == 0:
            idx += 1
            continue
        left = acc[ryotei_index[idx - 1]]
        right = acc[ryotei_index[idx]]
        res.append(dist_abs(left, right))
        idx += 1

    return sum(res)

if __name__ == "__main__":
    dists, ryo = data_req()
    result = search(dists, ryo)
    print(result % 100000)