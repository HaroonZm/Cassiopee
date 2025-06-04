import sys
import re

def main():
    # Nombre de serpents à identifier
    n = int(sys.stdin.readline().strip())

    # Expression régulière pour un serpent de type A
    # ^ >' (=+) # \1 ~ $
    # Détail :
    # ^ >'              : commence par >'
    # (=+)              : capture un ou plusieurs '='
    # #                 : suivi d'un '#'
    # \1                : suivi du même nombre d' '=' que précédemment (rappel du groupe 1)
    # ~                 : fini par un tilde '~'
    re_a = re.compile(r"^>'(=+)#\1~$")

    # Expression régulière pour un serpent de type B
    # ^ >\^ (Q=)+ ~~ $
    # Détail :
    # ^ >^             : commence par >^
    # (Q=)+            : une ou plusieurs répétitions de "Q="
    # ~~               : suivi de "~~" en fin
    re_b = re.compile(r"^>\^(Q=)+~~$")

    for _ in range(n):
        s = sys.stdin.readline().strip()

        # Test type A
        if re_a.match(s):
            print("A")
        # Test type B
        elif re_b.match(s):
            print("B")
        else:
            print("NA")

if __name__ == "__main__":
    main()