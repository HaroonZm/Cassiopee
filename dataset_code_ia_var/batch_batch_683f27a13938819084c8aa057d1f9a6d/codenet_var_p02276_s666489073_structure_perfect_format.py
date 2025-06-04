def InputData():
    sequence_len = int(input())
    sequence = list(map(int, input().split(" ")))
    return sequence_len, sequence

def partition(sequence, p, r):
    x = sequence[r]
    i = p - 1
    for j in range(p, r):
        if sequence[j] <= x:
            i += 1
            sequence[i], sequence[j] = sequence[j], sequence[i]
    sequence[i + 1], sequence[r] = sequence[r], sequence[i + 1]
    return i + 1

def PrintOut(sequence):
    print(' '.join(map(str, sequence)))

def main():
    sequence_len, sequence = InputData()
    q = partition(sequence, 0, sequence_len - 1)
    sequence[q] = "[" + str(sequence[q]) + "]"
    PrintOut(sequence)

if __name__ == "__main__":
    main()