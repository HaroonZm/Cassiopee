def process_input():
    data = input().split()
    # Style: Fonctionnelle & procédurale mélangées
    a = int(data[0])
    b = int(data[1])
    k = int(data[2])

    def adjust(val, sub):
        # Style: fonction imbriquée
        return val - sub if val - sub > 0 else 0

    ans_t = max(a - k, 0)

    # Style: ternaire imbriqué dans une assignation
    b_new = b if a - k >= 0 else max(0, b - (k - a))

    # Utilisation d'un print à la fin, mais tuple généré dans une liste par compréhension pour ajouter de la variété
    output = [ans_t, b_new]
    print(*output)

process_input()