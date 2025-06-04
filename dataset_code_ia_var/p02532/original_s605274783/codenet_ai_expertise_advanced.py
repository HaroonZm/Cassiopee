from sys import stdin

def main():
    n = int(input())
    blocks = [[] for _ in range(n)]
    pops = []

    for line in stdin:
        parts = line.split()
        match parts:
            case ["quit"]:
                print(*pops, sep='\n')
                return
            case ["push", i, val]:
                blocks[int(i)-1].append(val)
            case ["pop", i]:
                pops.append(blocks[int(i)-1].pop())
            case ["move", i, j]:
                blocks[int(j)-1].append(blocks[int(i)-1].pop())
            case _:
                continue

if __name__ == "__main__":
    main()