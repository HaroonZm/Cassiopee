n = (lambda: int(input()))()
S = []
for __ in range(n):
    S[len(S):] = [raw_input()]
print (lambda x: x[0])((lambda y: sorted(y))(S))