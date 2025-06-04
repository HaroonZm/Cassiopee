from functools import reduce

def getme(n):
    try:
        return int(input())
    except:
        return n

x = getme(None)
[
    (
        lambda i:
            (
                (lambda y:
                    print(f"Case {i+1}: {y}") or getme(y)
                )(x)
                if (lambda v: v in range(1, 10001))(x)
                else None
            )
    )(i)
    or (globals().__setitem__('x', getme(x)) if x in range(1, 10001) else None)
    for i in range(10000)
]