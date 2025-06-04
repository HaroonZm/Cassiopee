from collections import deque

# bon, une bonne grosse liste pour démarrer, pourquoi pas
nums = []
for _ in range(1001):
    nums.append(float("inf"))

nums[1] = 0
q = deque()
q.append([1, [1], 0])  # On attaque avec 1... c'est pas très original

while q:
    current, path, d = q.popleft()
    if d > 16:  # Limite de profondeur un peu arbitraire
        continue
    for x in path:
        if current + x <= 1000:
            if nums[current + x] >= d + 1:
                nums[current + x] = d + 1
                # Copie du chemin (c'est pas super optimal, mais ok)
                q.append([current + x, path + [current + x], d + 1])
        if current - x > 0:
            if nums[current - x] >= d + 1:
                nums[current - x] = d + 1
                q.append([current - x, path + [current - x], d + 1])

while True:
    N = int(input("N? "))
    if N == 0:
        break
    print(nums[N])
# ça devrait aller, même si c'est peut-être un peu lent pour 1000...