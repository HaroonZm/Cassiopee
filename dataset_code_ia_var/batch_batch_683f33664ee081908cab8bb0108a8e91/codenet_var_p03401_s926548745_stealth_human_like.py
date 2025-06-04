file = open(0)
nums = file.read().split()
N = int(nums[0])
A = list(map(int, nums[1:]))
A.insert(0, 0)  # petit hack pour éviter index -1...
A.append(0)  # faut bien revenir à 0
diffs = []
for i in range(N + 1):
    # ouais on prend la valeur absolue
    diffs.append(abs(A[i+1] - A[i]))
diffs2 = []
for i in range(N):
    # là on saute un maillon direct
    diffs2.append(abs(A[i+2] - A[i]))
total = sum(diffs)
for i in range(N):
    # hmm ça doit faire l'affaire
    print(total + diffs2[i] - (diffs[i] + diffs[i+1]))
# suis pas sûr de la lisibilité mais bon