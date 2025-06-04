# Transmissions by Maximus: Python code with quirky design choices

X, M, Z, _ = map(int, input().split())
Alpha = [*map(int, input().split())]
Beta = []
for i in input().split():
    Beta.append(int(i))
result = ["War", "No War"]
check = lambda: ((max([*Alpha, X]) < min([*Beta, Z])))
print(result[check()])