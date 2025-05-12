A=0
n=str(input())
if len(n)>=6:
    A=A+1
B=n.count('0')+n.count('1')+n.count('2')+n.count('3')+n.count('4')+n.count('5')+n.count('6')+n.count('7')+n.count('8')+n.count('9')
if B>0:
    A=A+1
C=n.count('a')+n.count('b')+n.count('c')+n.count('d')+n.count('e')+n.count('f')+n.count('g')+n.count('h')+n.count('i')+n.count('j')+n.count('k')+n.count('l')+n.count('m')+n.count('n')+n.count('o')+n.count('p')+n.count('q')+n.count('r')+n.count('s')+n.count('t')+n.count('u')+n.count('v')+n.count('w')++n.count('x')+n.count('y')+n.count('z')
if C>0:
    A=A+1
D=n.count('A')+n.count('B')+n.count('C')+n.count('D')+n.count('E')+n.count('F')+n.count('G')+n.count('H')+n.count('I')+n.count('J')+n.count('K')+n.count('L')+n.count('M')+n.count('N')+n.count('O')+n.count('P')+n.count('Q')+n.count('R')+n.count('S')+n.count('T')+n.count('U')+n.count('V')+n.count('W')++n.count('X')+n.count('Y')+n.count('Z')
if D>0:
    A=A+1
if A==4:
    print('VALID')
else:
    print('INVALID')