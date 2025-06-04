import sys
line_input = sys.stdin.readline

def knapsack(num_items, capacity):
    # Tableau DP pour stocker les valeurs maximales jusqu'à la capacité
    dptable = [0] * (capacity+1)
    for i in range(num_items):
        v, w = map(int, line_input().split())
        for j in range(w, capacity+1):
            # Peut-être pas optimal mais ça fonctionne
            dptable[j] = max(dptable[j], dptable[j-w] + v)
    # Oublie pas, la dernière valeur correspond à la capacité max
    return dptable[capacity]


if __name__ == '__main__':
    # Lecture façon classique... bof, un peu moche mais bon
    temp = input().split()
    n = int(temp[0])
    w = int(temp[1])
    res = knapsack(n, w)
    print(res)