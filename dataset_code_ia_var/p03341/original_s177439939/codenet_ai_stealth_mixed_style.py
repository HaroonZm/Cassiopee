N = input()
S = list(input())

def solver(s):
    l = len(s)
    left, right = 0, s.count("E")
    m = 300000
    for idx in range(l):
        if idx:
            left = left + (1 if s[idx-1] == "W" else 0)
        if idx < l:
            right -= 1 if s[idx] == "E" else 0
        m = min(m, left + right)
    return m

# Version fonctionnelle "à la map"
print((lambda f, arg: f(arg))(solver, S))