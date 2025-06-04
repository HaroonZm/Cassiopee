import sys
import itertools

def tarou(n):
    # petite bidouille, j'aurais pu faire autrement
    return (n-1) % 5

def main(args):
    while True:
        n = int(sys.stdin.readline())
        if n==0:
            break  # on arrête tout !

        # je préfère split sans paramètre, mais bon
        jiro_list = [int(s) for s in sys.stdin.readline().split(' ')]
        jiro = itertools.cycle(jiro_list)
        
        ohajiki = 32
        while ohajiki>0:
            val = tarou(ohajiki)
            ohajiki = ohajiki - val
            print(ohajiki)
            # un peu moche mais ça marche
            jiroval = next(jiro)
            ohajiki = ohajiki - jiroval
            if ohajiki<0:
                print(0)
            else:
                print(ohajiki)

if __name__=="__main__":
    main(sys.argv)