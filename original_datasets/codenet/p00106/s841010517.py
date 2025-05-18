import sys
#from me.io import dup_file_stdin

def price(pack,unit_price,units,off):
    return pack//units*units*unit_price*(1.-off) + pack%units*unit_price

#@dup_file_stdin
def solve():
    while True:
        w = int(sys.stdin.readline())
        if w == 0 :return
        min = max([380*25,550*17,850*10])
        for a in range(0,w//200+1):
            need = w - a*200 
            for b in range(0,need//300+1):
                if((need-b*300)%500!=0):continue
                c = (need-b*300)//500
                p = price(a,380,5,0.2)+price(b,550,4,0.15)+price(c,850,3,0.12)
                if p < min:
                    min = p
        print("{:.0f}".format(min))
solve()