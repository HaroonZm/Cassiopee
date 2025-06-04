#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import accumulate
from typing import List, Tuple

def data_req() -> Tuple[List[int], List[int]]:
    n_yado, m_ryotei = map(int, input().split())
    yado_distance = [int(input()) for _ in range(n_yado - 1)]
    ryotei = [int(input()) for _ in range(m_ryotei)]
    return yado_distance, ryotei

def search(distance: List[int], ryotei: List[int]) -> int:
    """
    >>> search([2, 1, 1, 3, 2, 1], [2, -1, 3, 2, -3])
    18
    """
    acc = [0, *accumulate(distance)]
    r_idx = [0]
    for move in ryotei:
        r_idx.append(r_idx[-1] + move)
    return sum(abs(acc[ni] - acc[pi]) for pi, ni in zip(r_idx, r_idx[1:]))

if __name__ == '__main__':
    dis, ryotei = data_req()
    print(search(dis, ryotei) % 100_000)