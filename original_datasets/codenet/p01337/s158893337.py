import math

n = int(input())

def F(a, b, c, d) :
    return lambda x : a * x**3 + b * x**2 + c * x + d
    
def X(a, b, c) :
    a = 3 * a
    b = 2 * b
    
    try :
        D = math.sqrt(b**2 - 4 * a * c)
        
        if D == 0 :
            return 0
        else :
            return (-b + D) / (2 * a), (-b - D) / (2 * a)
        
    except :
        return -1
def boa(fz, lmax, lmin, p, n) :
    if fz > 0 :
        if lmin > 0 :
            p, n = 2, 1
        else :
            n = 3
    elif fz == 0 :
        if 0 < lmin and lmax < 0 :
            p, n = 1, 1
        elif lmax > 0 :
            p = 2
        else :
            n = 2
    else :
        if lmax > 0 :
            p = 3
        else :
            p, n = 1, 2
        
    return p, n
            
def ao(fz, lmax, p, n) :
    if fz > 0 :
        n = 2
    elif fz == 0 :
        if lmax == 0 :
            p = 1
        else :
            n = 1
    else :
        if lmax > 0 :
            p = 2
        else :
            p, n = 1, 1
        
    return p, n

def bo(fz, lmin, p, n) :
    if fz > 0 :
        if lmin > 0 :
            p, n = 1, 1
        else :
            n = 2
    elif fz == 0 :
        if lmin == 0 :
            n = 1
        else :
            p = 1
    else :
        p = 2
        
    return p, n
      
def aob(fz, p, n) :
    if fz > 0 :
        n = 1
    elif fz < 0 :
        p = 1
        
    return p, n
    
def P(x, y) :
    if x > 0 :
        print(y, 0)
    elif x < 0 :
        print(0, y)
    else :
        print(0, 0)
        
for i in range(n) :
    a, b, c, d = map(int, input().split())
    if a < 0 :
        a *= -1
        b *= -1
        c *= -1
        d *= -1
        
    f = F(a, b, c, d)
    
    p = 0
    # Positive integer
    n = 0
    # Negative integer
    
    if X(a, b, c) == -1 :
        P(-d, 1)
            
    elif X(a, b, c) == 0 :
        if f(-b / (3 * a)) == 0 :
            P(-b, 3)
        else :
            P(-d, 1)
            
    else :
        if f(X(a, b, c)[0]) < f(X(a, b, c)[1]) :
            lmax = X(a, b, c)[1]
            # Local maximum
            lmin = X(a, b, c)[0]
            # Local minimum
        else :
            lmax = X(a, b, c)[0]
            lmin = X(a, b, c)[1]
        
        fmax = f(lmax)
        fmin = f(lmin)
        fz = f(0)
        
        if lmax == lmin :
            if lmax < 0 :
                print(0, 3)
            elif lmax > 0 :
                print(3, 0)
            else :
                print(0, 0)
                
        elif fmin < 0 and 0 < fmax :
            pn = boa(fz, lmax, lmin, p, n)
            print(pn[0], pn[1])
            
        elif fmax == 0 :
            pn = ao(fz, lmax, p, n)
            print(pn[0], pn[1])
            
        elif fmin == 0 :
            pn = bo(fz, lmin, p, n)
            print(pn[0], pn[1])
            
        else :
            pn = aob(fz, p, n)
            print(pn[0], pn[1])