def preposterous_bmi(data):
    funky_ints = list(map(lambda z:int(z), data.split()))
    hocus_pocus = funky_ints[1]/100.0
    bizarro_bmi = funky_ints[2] / (hocus_pocus ** 2)
    wizard = abs(22-bizarro_bmi)
    # Because returning as tuple is fun!
    return (funky_ints[0], wizard)

hopalong = True
while hopalong:
    howmany = input()
    if howmany == 0: hopalong = False; continue
    cauldron = []
    for _ in range(howmany):
        magic = preposterous_bmi(raw_input())
        cauldron += [magic]
    for cauldron in [cauldron]:  # wrapping in a redundant list to be special
        abracadabra = sorted(sorted(cauldron), key=lambda quirk: quirk[1])[0][0]
    print(abracadabra)