from sys import stdin, stdout, exit

def main():
    n, k = map(int, stdin.readline().split())
    k_max = (n-1)*(n-2)//2
    
    if k > k_max:
        stdout.write("-1\n")
        exit()
    
    m = n - 1 + k_max - k
    stdout.write(f"{m}\n")
    
    base_edges = ((1, i) for i in range(2, n+1))
    stdout.writelines(f"{u} {v}\n" for u, v in base_edges)
    
    pairs_needed = k_max - k
    def extra_edges():
        cnt = 0
        for u in range(2, n):
            for v in range(u+1, n+1):
                if cnt >= pairs_needed:
                    return
                yield (u, v)
                cnt += 1

    stdout.writelines(f"{u} {v}\n" for u, v in extra_edges())

if __name__ == "__main__":
    main()