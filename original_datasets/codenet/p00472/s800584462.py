# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 木 11/ 9 19:01:14 2017

# Usage
#
"""
from itertools import accumulate

def data_req():
    n_yado, m_ryotei = [int(i) for i in input().split(" ")]
    yado_distance = []
    ryotei = []
    for _ in range(n_yado - 1):
        yado_distance.append(int(input()))
    for _ in range(m_ryotei):
        ryotei.append(int(input()))

    return yado_distance, ryotei

def search(distance, ryotei):
    """search.

    >>> search([2, 1, 1, 3, 2, 1], [2, -1, 3, 2, -3])
    18
    """
    acc = [0] + list(accumulate(distance, lambda x, y: x+y))
    ryotei_index = [0] + list(accumulate(ryotei, lambda x, y: x+y))
    # print(ryotei_index)
    res = []
    for index in enumerate(ryotei_index):
        if index[0] == 0:
            continue
        index = index[0]
        # print(index)
        # print(ryotei_index[index])
        # print(ryotei_index[index - 1])
        dist = abs(acc[ryotei_index[index]] - acc[ryotei_index[index - 1]])
        res.append(dist)
        # print(sum(res))
    # his = []
    #
    # for index in range(len(ryotei_index)):
    #     his.append(acc[ryotei_index[index + 1]] - acc[ryotei_index[index]])
    #
    # return sum(his)
    return sum(res)

if __name__ == '__main__':
    dis, ryotei = data_req()
    print(search(dis, ryotei) % 100000)