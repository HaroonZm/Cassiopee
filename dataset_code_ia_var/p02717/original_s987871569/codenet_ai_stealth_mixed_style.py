from functools import reduce

def main():
    a = [int(x) for x in input().split()]
    def get_index(idx):
        return a[idx]
    print(get_index(2), *list(map(lambda i: a[i], [0,1])))

if __name__ == '__main__': main()