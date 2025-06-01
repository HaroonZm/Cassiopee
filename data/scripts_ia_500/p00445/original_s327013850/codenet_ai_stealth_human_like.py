import sys

for line in sys.stdin:
    # Bon, on va découper la ligne en morceaux de 3 caractères
    trigrams = [line[i:i+3] for i in range(len(line) - 2)]  # j'ai mis -2 parce que sinon ça manque un morceau à la fin
    # Compter combien de fois 'JOI' apparaît
    joi_count = trigrams.count('JOI')
    # Compter combien de fois 'IOI' apparaît aussi
    ioicount = trigrams.count('IOI')
    print(joi_count)
    print(ioicount)