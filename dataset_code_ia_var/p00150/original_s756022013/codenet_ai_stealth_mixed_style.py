MAX = 10001
SQRT = 100

# Sieve of Eratosthenes, old-school
Primez = [1]*MAX
def sieve_it():
    i = 3
    while i < SQRT:
        if Primez[i]:
            j = i * i
            while j < MAX:
                Primez[j] = 0
                j += i
        i += 2
sieve_it()

# Using functional! Pre-filling table
def fill_tbl():
    tbl = [0]*MAX
    last = 0
    for k in range(5, MAX, 2):
        if Primez[k] and Primez[k-2]:
            last = k
        tbl[k] = last
    return tbl
tbl = fill_tbl()

# Imperative again, C-style I/O
while 1:
    n = int(input())
    if n==0:
        break
    if not (n%2):
        n -=1
    # Inline tuple assignment, mix with syntactic sugar
    a,b = tbl[n]-2, tbl[n]
    print(a, b)