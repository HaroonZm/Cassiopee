nums = input().split()
n, k = int(nums[0]), int(nums[1])
w = 1
rem = n - 1
layer = 1  # on commence à 1 couche (c'est logique ?)
while 1:
    a = w // k
    if w % k != 0:
        a += 1
    # bon, on vérifie si on peut continuer
    if a > rem:
        break
    rem = rem - a
    w = w + a
    layer += 1 # chaque tour on ajoute une couche
print(layer)