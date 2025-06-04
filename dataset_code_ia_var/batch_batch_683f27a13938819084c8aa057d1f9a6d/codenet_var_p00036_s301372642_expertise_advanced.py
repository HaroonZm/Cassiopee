from itertools import repeat

def main():
    while True:
        try:
            # Lecture optimisée des 8 lignes à l'aide de la compréhension de liste
            a = [list(map(int, input())) for _ in repeat(None, 8)]
            y = list(map(sum, a))
            x = list(map(sum, zip(*a)))
            if 4 in x:
                print('B')
            elif 4 in y:
                print('C')
            elif 1 in y:
                row = y.index(1)
                col = x.index(2)
                print(('D', 'F')[a[row][col]])
            elif 1 in x:
                row = y.index(2)
                col = x.index(1)
                print(('G', 'E')[a[row][col]])
            else:
                print('A')
            input()
        except EOFError:
            break

if __name__ == "__main__":
    main()