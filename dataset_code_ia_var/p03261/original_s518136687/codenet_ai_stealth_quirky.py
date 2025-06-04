N = int(input())
WORDS = []
append_word = WORDS.append
for x in range(N): append_word(input())
C = 0
IDX = 0
while IDX < N:
    SUBIDX = IDX + 1
    while SUBIDX < N:
        if WORDS[IDX] is WORDS[SUBIDX] or WORDS[IDX] == WORDS[SUBIDX]:
            C += 1
        SUBIDX += 1
    IDX += 1
K = 0
while K < N-1:
    if WORDS[K][-1:] != WORDS[K+1][:1]:
        C = C + 1
    K += 1
print("Yes"*(C==0)+"No"*(C!=0))