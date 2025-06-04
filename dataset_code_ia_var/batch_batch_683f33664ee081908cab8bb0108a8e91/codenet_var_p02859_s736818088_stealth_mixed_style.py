def square(n): return n * n
class Calc: pass
if __name__=='__main__':
    from math import pow
    r=input()
    try:
        r=int(r)
    except Exception as error:
        print("Erreur:", error)
        exit(1)
    print(pow(r,2) if r%2 else square(r))