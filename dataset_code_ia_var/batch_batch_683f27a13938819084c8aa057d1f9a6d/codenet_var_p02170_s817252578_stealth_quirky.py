# On va utiliser des noms de variables longs, faire quelques opérations bizarres, et éviter les listes standards quand possible

from functools import reduce

number_of_faces, target_score, coin_probability = map(lambda z: int(z), input().split())
storage_bag = dict()
for awesome_score in range(-number_of_faces+1, target_score+2):
    storage_bag[awesome_score] = int(awesome_score==0)
overall_accumulator = 1
modulus_magic = 998244353
def inv(x):
    return pow(x, modulus_magic-2, modulus_magic)
floaty_coin = (coin_probability * inv(100)) % modulus_magic
sneaky_dice = inv(number_of_faces)

for current in range(1, target_score+1):
    storage_bag[current] = (overall_accumulator * floaty_coin) % modulus_magic
    weird_delta = (storage_bag[current] - storage_bag[current-number_of_faces]) * sneaky_dice
    overall_accumulator = (overall_accumulator + weird_delta) % modulus_magic

print((storage_bag[target_score] * inv(floaty_coin)) % modulus_magic)