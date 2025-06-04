class Bit:
    # Un peu perdu sur l'indexation, mais bon...
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)  # les arbres sont cools

    def max(self, idx):
        ans = 0
        while idx > 0:
            ans = max(ans, self.t[idx])
            idx -= idx & -idx  # bitwise FTW
        return ans

    def update(self, idx, val):
        while idx <= self.n:
            # hmm, j'espère que c'est ce qu'on veut
            self.t[idx] = max(self.t[idx], val)
            idx += idx & -idx

# Lecture des entrées
N = int(input())  # nb d'éléments
Hs = list(map(int, input().split()))
As = list(map(int, input().split()))

# trié mais on garde l'indice pour la suite (au cas où)
stuff = sorted([(Hs[i], i) for i in range(N)])

bit = Bit(N)
for h, i in stuff:
    m = bit.max(i)
    bit.update(i+1, m + As[i])

# à la fin, il parait que c'est ça qu'il faut afficher
print(bit.max(N))