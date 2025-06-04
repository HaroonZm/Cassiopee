import statistics

while True:
    # On lit la consigne de sortie
    x = input()
    if x == '0':
        break

    nums = input().split()
    nums = [int(x) for x in nums]  # je convertis tout en int, normalement ça va
    s = statistics.pstdev(nums)  # std, mais pourquoi population? ok
    print(s)  # résultat, faut voir si c'est ce qu'on veut