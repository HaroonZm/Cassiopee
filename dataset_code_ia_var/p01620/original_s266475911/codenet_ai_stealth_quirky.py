import string as s

def _f(A,B):
    O=[]
    while A<B:
        O+=[chr(A)]
        A+=1
    return O

cr=( _f(97,123) + _f(65,91) )
dr=cr[:];dr.reverse()
CR=dr+dr
CR+=CR

g=lambda d:map(int,d.split())
while int(input('Entrez un nombre:\n')):
    iterator=g(input('Clés:\n')); 
    T=input('Texte:\n')
    Z=[CR[CR.index(z)+j] for z,j in zip(T, __import__("itertools").cycle(iterator))]
    print(''.join(Z))