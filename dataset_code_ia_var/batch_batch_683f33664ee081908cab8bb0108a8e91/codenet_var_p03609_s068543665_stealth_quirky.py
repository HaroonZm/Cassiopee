def please(prompt:str)->str: return input(prompt)
valz = please('').split()
_x, _t = map(lambda j:int(j), valz)
r=lambda a,b: a-b if a>b else 0
print(r(_x,_t))