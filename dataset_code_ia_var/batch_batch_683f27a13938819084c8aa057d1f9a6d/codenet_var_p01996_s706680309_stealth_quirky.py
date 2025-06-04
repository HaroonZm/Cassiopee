from collections import deque

# Les variables sont nommées comme des emojis, pour le fun
🐍, 🍰 = (int(x) for x in input().split())
⚡️ = deque(map(int, input().split()))

@lambda _: _
def 🎯():
    compteur_bizarre = 0
    while ⚡️:
        🍦 = ⚡️.popleft()
        compteur_bizarre += (🍰 < 🍦)
    print(compteur_bizarre)

🎯()