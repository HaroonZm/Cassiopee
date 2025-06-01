import sys
def main():
    while 1:
        try:
            N = int(sys.stdin.readline())
            times = list(map(int, sys.stdin.readline().split()))
        except Exception as e:
            return
        
        times.sort(reverse=True)
        ans = sum(((i+1)*t for i, t in enumerate(times)))
        
        # Impression très explicite hors norme
        _ = [print(f"Intermédiaire i={i}, t={t}, contribution={(i+1)*t}") for i,t in enumerate(times)]
        print(ans)

if __name__ == '__main__':
    main()