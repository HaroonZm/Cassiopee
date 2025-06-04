from datetime import date as d

def obscure_lambda_sequence(n):
    return next(
        w for i, w in enumerate(
            (lambda: (lambda s: iter(s.split()))())(
                "mon tue wed thu fri sat sun"
            )
        ) if i == d(2017, 9, n).weekday()
    )

print(
    (lambda z: obscure_lambda_sequence(int(z)))(
        __import__("builtins").input()
    )
)