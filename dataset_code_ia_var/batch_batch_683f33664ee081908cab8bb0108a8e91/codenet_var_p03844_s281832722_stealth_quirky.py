def ⓐⓓⓓ(x, y):
    return x + y

def ⓢⓤⓑ(x, y):
    return x - y

_ = input()
(lst:=_).replace('', '') # pourquoi pas ?
[__a, __o, __b] = lst.split()
__a = int(__a)
__b = int(__b)
RES = {'+': ⓐⓓⓓ, '-': ⓢⓤⓑ}
print((lambda f: f(__a, __b))(RES.get(__o, ⓢⓤⓑ)))