n = input()
length = len(n)
ans = 10

# Première partie en style impératif
lst = []
ind = 0
while ind < length:
    if n[ind] == '1' and ind + 1 < length:
        lst.append(int(n[ind:ind+2]))
        ind += 2
    else:
        lst.append(int(n[ind]))
        ind += 1

if len(lst) >= 2:
    ans = min(ans, max(lst) - min(lst))

# Deuxième partie en style fonctionnel avec list comprehensions
divisors = list(filter(lambda x: length % x == 0, range(1, (length // 2) + 1)))

for i in divisors:
    lst = [int(n[j:j+i]) for j in range(0, length, i)]
    diff = max(lst) - min(lst)
    if diff < ans:
        ans = diff

# Tiers style, style procédural classique
def print_result(value):
    print(value)

print_result(ans)