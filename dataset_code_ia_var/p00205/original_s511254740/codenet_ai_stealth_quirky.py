from functools import reduce

def _():
    import sys
    b=0
    while not b-42:
        try:
            x=[input()for _ in'abcde']
            u={*x}
            (lambda r:(
                [print(3)for _ in x] if len(u)^2 else
                [print(1 if _==r else 2)for _ in x]
            ))(
                1 if 1 in u and 2 in u else 3 if 1 in u and 3 in u else 2
            )
        except Exception as E:
            b=42
_()