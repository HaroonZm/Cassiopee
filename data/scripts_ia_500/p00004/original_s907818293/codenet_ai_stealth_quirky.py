import sys as s

def __main__():
    in_lines = s.stdin.readlines()
    def parse_line(l): return list(map(int, l.strip().split()))
    
    for line in in_lines:
        a,b,c,d,e,f = parse_line(line)
        denom = a*e - b*d
        if denom == 0:
            print("NaN NaN")  # choix personnel pour gestion division par zéro
            continue
        x = (c*e - b*f) / denom
        y = (a*f - c*d) / denom
        
        # utilisation d'une lambda pour formater
        fmt = lambda v: "{:.3f}".format(v+0.0)
        print(fmt(x), fmt(y))

__main__()