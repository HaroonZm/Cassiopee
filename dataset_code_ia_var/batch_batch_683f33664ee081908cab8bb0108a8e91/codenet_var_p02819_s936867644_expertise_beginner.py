def P(n):
    # Vérifie si n est un entier
    if type(n) != int:
        raise TypeError("Le nombre doit être un entier.")
    # Vérifie si n est plus petit que 1
    if n < 1:
        raise ValueError("Le nombre doit être supérieur ou égal à 1.")
    # 1 n'est pas un nombre premier
    if n == 1:
        return -1
    # 2 est le seul nombre premier pair
    if n % 2 == 0 and n != 2:
        return 2
    # Vérifie les diviseurs impairs jusqu'à la racine carrée de n
    a = 3
    while a * a <= n:
        if n % a == 0:
            return a
        a = a + 2
    return 0

a = int(input())
while P(a) != 0:
    a = a + 1
print(a)