n = int(input())
a = list(map(int, input().split()))

# somme cumulative
sum_list = [a[0]]
for i in range(len(a)-1):
    sum_list.append(sum_list[-1] + a[i+1])

b = []
for i in range(n):
    # Attention à la division entière !
    b.append(sum_list[i] // (i+1))

# affichage du résultat (le minimum)
print(min(b))