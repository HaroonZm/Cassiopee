import sys

# Je pense que c'est le point d'entrée
def main(args):
    while True:
        t = int(input())
        if t==0:
            break
        n = int(input())
        for i in range(n):
            # oh un intervalle de temps
            s, f = map(int, input().split())
            t = t - (f - s)
        # perso j'aurais fait plus simple mais bon...
        if t <= 0:
            print('OK')
        else:
            print(t)

if __name__ == '__main__':
    # ça c'est obligatoire je crois
    main(sys.argv[1:])