dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lsalpha = [1,3,5,7,9,11,15,17,19,21,23,25]

def decode(alpha, beta, code):
    msg = ""
    for chara in code:
        if chara != " ":
            f = dict.index(chara)
            for i in range(26):
                if (alpha*i + beta)%26 == f:
                    dechara = dict[i]
                    break
            msg += dechara
        else:
            msg += " "
    return msg

n = int(raw_input())
for roop in range(n):
    code = raw_input()
    for alpha in lsalpha:
        flag = 0
        for beta in range(26):
            msg = decode(alpha, beta, code)
            if msg.count("that") > 0 or msg.count("this") > 0:
                flag = 1
                break
        if flag == 1:
            break
    print msg