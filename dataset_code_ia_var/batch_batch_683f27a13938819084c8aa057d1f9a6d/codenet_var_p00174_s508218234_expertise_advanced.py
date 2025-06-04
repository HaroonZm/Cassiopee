from collections import Counter
from itertools import islice

def process_items():
    while True:
        items = list(islice(lambda: input(), 3))
        if not items or items[0] == "0":
            break
        for item in items:
            c = Counter(item)
            c[item[0]] -= 1
            key = "A" if c["A"] > c["B"] else "B"
            c[key] += 1
            print(f"{c['A']} {c['B']}")

process_items()