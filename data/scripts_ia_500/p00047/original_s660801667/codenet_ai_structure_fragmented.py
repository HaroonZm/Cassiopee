import sys

def lire_lignes():
    return sys.stdin

def traiter_ligne(line):
    return line.rstrip("\n").split(",")

def echanger_elements(fe, i, j):
    tmp = fe[i]
    fe[i] = fe[j]
    fe[j] = tmp

def index_de_A(fe):
    return fe.index("A")

def swap_A_B(fe):
    echanger_elements(fe, 0, 1)

def swap_A_C(fe):
    echanger_elements(fe, 0, 2)

def swap_B_A(fe):
    echanger_elements(fe, 1, 0)

def swap_B_C(fe):
    echanger_elements(fe, 1, 2)

def swap_C_A(fe):
    echanger_elements(fe, 0, 2)

def swap_C_B(fe):
    echanger_elements(fe, 1, 2)

def traiter_instructions(fe, instructions):
    for line in instructions:
        num = traiter_ligne(line)
        if num[0] == "A":
            if num[1] == "B":
                swap_A_B(fe)
            else:
                swap_A_C(fe)
        elif num[0] == "B":
            if num[1] == "A":
                swap_B_A(fe)
            else:
                swap_B_C(fe)
        elif num[0] == "C":
            if num[1] == "A":
                swap_C_A(fe)
            else:
                swap_C_B(fe)

def afficher_position_A(fe):
    pos = index_de_A(fe)
    if pos == 0:
        print("A")
    elif pos == 1:
        print("B")
    else:
        print("C")

def main():
    fe = ["A", "B", "C"]
    instructions = lire_lignes()
    traiter_instructions(fe, instructions)
    afficher_position_A(fe)

main()