table = {
    "11":"a","12":"b","13":"c","14":"d","15":"e",
    "21":"f","22":"g","23":"h","24":"i","25":"j",
    "31":"k","32":"l","33":"m","34":"n","35":"o",
    "41":"p","42":"q","43":"r","44":"s","45":"t",
    "51":"u","52":"v","53":"w","54":"x","55":"y","56":"z",
    "61":".","62":"?","63":"!","64":" "
}

import sys

for line in sys.stdin:
    s = line.strip()
    if len(s) % 2 != 0:
        print("NA")
        continue
    result = ""
    ok = True
    for i in range(0, len(s), 2):
        code = s[i:i+2]
        if code in table:
            result += table[code]
        else:
            ok = False
            break
    if ok:
        print(result)
    else:
        print("NA")