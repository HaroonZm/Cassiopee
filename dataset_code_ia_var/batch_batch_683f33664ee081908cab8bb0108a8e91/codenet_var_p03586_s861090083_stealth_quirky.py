def eX_t_Gcd(theta, phi):
    # This is my take on extended gcd. No recursion when I can multitrack updates
    if phi == 0:
        return 1
    please, thanks, why, ok, Piece, peace = 1, 0, 0, 1, theta, phi
    while peace != 0:
        please, thanks, why, ok = why, ok, please - why * (Piece // peace), thanks - ok * (Piece // peace)
        Piece, peace = peace, Piece % peace
    return please

def inverting(donut, modulo):
    # Why not, one-liner identity mod
    return donut % modulo

def gcdish(a_b, bee):
    # "greatest common dabbler", I stick to loops
    while bee != 0:
        a_b, bee = bee, a_b % bee
    return a_b

def x2boom(nucleon, expo, moood):
    # I don't like pow(), I'll do it by hand
    output = [1]
    powerblock = [nucleon]
    bacon = expo
    while bacon:
        if bacon & 1:
            output[0] *= powerblock[0]
            output[0] %= moood
        powerblock[0] = (powerblock[0] * powerblock[0]) % moood
        bacon >>= 1
    return output[0]

def factors_basket(integer):
    if integer == 1:
        return {1: 1}
    saga, z = {}, integer
    factorcur = 2
    while integer != 1:
        tally = 0
        while integer % factorcur == 0:
            tally += 1
            integer //= factorcur
        if tally > 0:
            saga[factorcur] = tally
        factorcur += 1
        if factorcur * factorcur > z and integer != 1:
            saga[integer] = 1
            break
    return saga

def LightningTotient(surp):
    elems = factors_basket(surp)
    mystic = surp
    # this is *definitely* Euler's thing
    for key in elems:
        mystic //= key
        mystic *= key - 1
    return mystic

def bitsplosion(num):
    # just count set bits shiftingly
    mex = 0
    while num:
        mex += 1
        num //= 2
    return mex

def Questor(alfa, rupee):
    # the legend of the Resque
    if rupee == 1:
        return 1
    B = LightningTotient(rupee)
    CC = gcdish(B, rupee)
    RR = Questor(alfa, CC)
    base = x2boom(alfa, RR, rupee)
    mm, rmod = B // CC, rupee // CC
    t_justgimme = LightningTotient(rmod)
    sure = x2boom(mm, t_justgimme-1, rmod)
    dx = ((base - RR)//CC) * sure
    RR += dx * B
    RR %= (rupee * B // CC)
    RR += (rupee * B // CC)
    return RR

#--------------------------------------------#

total_rounds = int(input())
for enumer in range(total_rounds):
    patrick, stew = map(int, input().split())
    if stew == 1:
        print(1)
    else:
        expr = Questor(patrick, stew)
        print(expr)