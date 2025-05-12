class Fermat:
    
    def __init__(self, size, mod):
        self.size = size
        self.mod = mod
        self.factorial = [1]
        self.inverse = [1]
        pre_f = 1
        for i in range(1, self.size+1):
            pre_f = (pre_f * i) % self.mod
            self.factorial.append(pre_f)
            self.inverse.append(pow(pre_f, self.mod-2, self.mod))
    
    def comb(self, n, r):
        if n < r:
            return 0
        else:
            return (self.factorial[n] * self.inverse[r] * self.inverse[n-r]) % self.mod
        
    def perm(self, n, r):
        if n < r:
            return 0
        else:
            return (self.factorial[n] * self.inverse[n-r]) % self.mod
      
if __name__ == "__main__":
    Fermat = Fermat(1000, 10**9+7)
    n, k = [int(i) for i in input().split()]
    print(Fermat.perm(k, n))