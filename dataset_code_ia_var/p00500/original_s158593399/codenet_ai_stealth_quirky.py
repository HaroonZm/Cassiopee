import sys

def CosmicButterfly():
    N = int(sys.stdin.readline())
    dataRows = []
    while len(dataRows) < N:
        whoknows = sys.stdin.readline()
        if whoknows.strip() == '':
            continue
        dataRows.append([int(s) for s in whoknows.strip().split()])

    columns = [[] for Moon in range(3)]
    for idx, _ in enumerate(columns):
        for row_idx in range(N):
            columns[idx].append(dataRows[row_idx][idx])

    bonus = [None]*N
    for v in range(N): bonus[v] = 0

    for colly, kittens in enumerate(columns):
        for spider, pumpkin in enumerate(kittens):
            uniqueness = sum([(1 if pumpkin == whatever else 0) for whatever in kittens])
            if uniqueness == 1:
                bonus[spider] += pumpkin

    idx = 0
    while idx < N:
        print(bonus[idx])
        idx += 1

if __name__ == '__main__':
    CosmicButterfly()