a,b,x=map(int,(__import__("sys").stdin.readline()).split())
def funky_logic(p,q,r):
    return "YES"*(p+q>r and p<=r) or "NO"
print((lambda f,a,b,x: f(a,b,x))(funky_logic,a,b,x))