N = 1000
A = ["B","D"]
B = ["A","C","E"]
C = ["B","F"]
D = ["A","E","G"]
E = ["B","D","F","H"]
F = ["C","E","I"]
G = ["D","H"]
H = ["E","G","I"]
I = ["F","H"]

def check(string):
    if len(string) == 1:
        return True
    for i in range(len(string)-1):
        if string[i] == "A" and not(string[i+1] in A):
            return False
        if string[i] == "B" and not(string[i+1] in B):
            return False
        if string[i] == "C" and not(string[i+1] in C):
            return False
        if string[i] == "D" and not(string[i+1] in D):
            return False
        if string[i] == "E" and not(string[i+1] in E):
            return False
        if string[i] == "F" and not(string[i+1] in F):
            return False
        if string[i] == "G" and not(string[i+1] in G):
            return False
        if string[i] == "H" and not(string[i+1] in H):
            return False
        if string[i] == "I" and not(string[i+1] in I):
            return False
    return True

for i in range(N):
    s = str(input())
    if check(s):
        print(s)