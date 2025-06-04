from functools import partial

a, b, c, d = map(int, input().split())
outcome = {
    'A': partial(print, "Alice"),
    'B': partial(print, "Bob"),
    'D': partial(print, "Draw")
}

if -1 in (c, d):
    outcome['A' if a < b else 'B' if a > b else 'D']()
else:
    outcome['A' if c > d else 'B' if c < d else 'D']()