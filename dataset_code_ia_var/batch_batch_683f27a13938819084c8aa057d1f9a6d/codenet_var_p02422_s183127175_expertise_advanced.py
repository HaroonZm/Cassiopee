from typing import Callable

def my_print(s: str, args: list[int]) -> str:
    start, end = map(int, args[:2])
    return s[start:end+1]

def my_reverse(s: str, args: list[int]) -> str:
    start, end = map(int, args[:2])
    end += 1
    return f"{s[:start]}{s[start:end][::-1]}{s[end:]}"

def my_replace(s: str, args: list[str]) -> str:
    start, end = map(int, args[:2])
    return f"{s[:start]}{args[2]}{s[end+1:]}"

def resolve():
    s = input()
    n = int(input())
    op_map: dict[str, Callable] = {
        'print': my_print,
        'reverse': my_reverse,
        'replace': my_replace,
    }

    for _ in range(n):
        f, *args = input().split()
        if f == 'print':
            print(op_map[f](s, args))
        else:
            s = op_map[f](s, args)

resolve()