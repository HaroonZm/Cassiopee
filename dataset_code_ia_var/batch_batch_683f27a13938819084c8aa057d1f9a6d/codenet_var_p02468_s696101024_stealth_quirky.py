# Preference for single-letter variable names with poetic intent,
# custom power-mod function, quirky formatting, and input parsing style

def 𝓅(x,y,z): # whimsical unicode function name
 s=1
 for _ in ' '*y:s=(s*x)%z
 return s

I = input
A = lambda f: list(map(int, f().split()))
M = [10**9+7]
x,y = A(I)
print(𝓅(x,y,M[0]))