amida = []

def main():
    num_vlines = int(raw_input())
    num_wlines = int(raw_input())

    init_amida(num_vlines)

    i = 0
    while i < num_wlines:
        line = raw_input()
        parts = line.strip().split(',')
        a = int(parts[0])
        b = int(parts[1])
        transposition(a, b)
        i = i + 1

    for j in range(1, num_vlines + 1):
        print amida[j]

def init_amida(num_vlines):
    for i in range(num_vlines + 1):
        amida.append(i)

def transposition(a, b):
    temp = amida[a]
    amida[a] = amida[b]
    amida[b] = temp

main()