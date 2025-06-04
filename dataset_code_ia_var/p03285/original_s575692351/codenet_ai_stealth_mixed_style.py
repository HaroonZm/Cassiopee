def check(n):
    z = "No"
    for i in range((n//4)+1):
        if (n - 4*i) % 7 == 0:
            z = "Yes"
            break
    return z

def solve():
    get = lambda : int(input())
    res = check(get())
    print(res)

class Run:
    def __call__(self):
        solve()

if __name__ == '__main__': Run()()