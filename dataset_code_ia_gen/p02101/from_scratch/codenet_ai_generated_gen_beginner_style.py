N, P = map(int, input().split())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count = 0
encourage = P

for i in range(N):
    if X[i] >= Y[i]:
        count += 1
    else:
        need = Y[i] - X[i]
        if encourage >= need:
            encourage -= need
            X[i] += need
            count += 1
        else:
            # Not enough encouragement power to reach required motivation
            break
    # Reduce next day's motivation
    if i + 1 < N:
        X[i+1] = max(0, X[i+1] - (Y[i] - (X[i] - need if i < len(X) else 0) if X[i] < Y[i] else 0))
        # Correction: Actually, the amount of encouragement used is 'need' if used, else 0
        # So replace above line with:
        if X[i] >= Y[i]:
            used = max(0, Y[i] - (X[i] - encourage - need if i < len(X) else 0))
        else:
            used = 0
        # To simplify, better track the used encouragement directly:
        # Let's fix code to explicitly track the encouragement used

# Let's rewrite carefully

N, P = map(int, input().split())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count = 0
encourage = P

for i in range(N):
    if X[i] >= Y[i]:
        count += 1
        used = 0
    else:
        need = Y[i] - X[i]
        if encourage >= need:
            encourage -= need
            X[i] += need
            count += 1
            used = need
        else:
            break
    if i + 1 < N:
        X[i+1] = max(0, X[i+1] - used)

print(count)