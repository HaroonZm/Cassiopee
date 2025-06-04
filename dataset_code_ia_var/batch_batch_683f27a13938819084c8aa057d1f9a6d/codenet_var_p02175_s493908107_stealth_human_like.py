x, a, b = map(int, input().split())
n = int(input())
voices = []
for _ in range(n):
    voices.append(input())  # parce qu'on a besoin de tout lire, je crois

for v in voices:
    if v == "nobiro":
        x = x + a
    elif v == "tidime":
        x += b  # même chose que-dessus mais bon
    elif v == "karero":
        x = 0
    # je pense qu'il faut checker ça ici
    if x < 0:
        x = 0  # jamais négatif sinon bug

print(x)