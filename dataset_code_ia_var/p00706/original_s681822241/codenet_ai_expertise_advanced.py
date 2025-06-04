from sys import stdin
from typing import List, Set, Tuple, Any
from dataclasses import dataclass

def get_data() -> int:
    return int(stdin.readline())

def get_data_list() -> List[int]:
    return list(map(int, stdin.readline().split()))

@dataclass(frozen=True)
class Position:
    w: int
    h: int

def get_all_persimmon_coordinate(persimmon_num: int) -> Set[Tuple[int, int]]:
    return {tuple(map(int, stdin.readline().split())) for _ in range(persimmon_num)}

def make_persimmon_map(area_size: Position, persimmons: Set[Tuple[int, int]]) -> List[List[int]]:
    w, h = area_size.w, area_size.h
    ps_map = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(1, h + 1):
        row_sum = 0
        for x in range(1, w + 1):
            row_sum += (x, y) in persimmons
            ps_map[y][x] = ps_map[y - 1][x] + row_sum
    return ps_map

def get_max_num(persimmon_map: List[List[int]], area_size: Position, given_size: Position) -> int:
    w, h = area_size.w, area_size.h
    gw, gh = given_size.w, given_size.h
    return max(
        calculate_persimmon_num(persimmon_map, w2, h2, gw, gh)
        for w2 in range(gw, w + 1)
        for h2 in range(gh, h + 1)
    )

def calculate_persimmon_num(persimmon_map: List[List[int]], w: int, h: int, gw: int, gh: int) -> int:
    return (
        persimmon_map[h][w]
        - persimmon_map[h - gh][w]
        - persimmon_map[h][w - gw]
        + persimmon_map[h - gh][w - gw]
    )

def main():
    while (persimmon_num := get_data()):
        area_size = Position(*get_data_list())
        persimmons = get_all_persimmon_coordinate(persimmon_num)
        given_size = Position(*get_data_list())
        ps_map = make_persimmon_map(area_size, persimmons)
        print(get_max_num(ps_map, area_size, given_size))

if __name__ == "__main__":
    main()