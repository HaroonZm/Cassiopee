print(
    next(
        (
            "vowel"
            for _ in iter(lambda: input(), object())
            if __import__("functools").reduce(lambda x, y: x or y, (ch == _ for ch in "aiueo"))
        ),
        "consonant"
    )
)