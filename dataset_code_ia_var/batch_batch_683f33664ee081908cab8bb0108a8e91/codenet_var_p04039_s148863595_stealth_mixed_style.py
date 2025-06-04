def start():
    N_K = input().strip().split()
    N = N_K[0]
    K = int(N_K[1])
    D = set(int(x) for x in input().split())
    usable = []
    for i in range(10):
        if i not in D:
            usable.append(str(i))
    def is_valid(number):
        for c in str(number):
            if c not in usable:
                return False
        return True
    n = int(N)
    found = False
    while not found:
        if is_valid(n):
            print(n)
            return
        n += 1

if __name__ == "__main__":
    lambda_func = (lambda: start())
    lambda_func()