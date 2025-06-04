def read_key():
 input_key = input()
 try:
  return int(input_key)
 except:
  return 0

map_char = lambda x: (26-(ord(x)-97))%26

def gen_lst(chars):
    res = []
    i = 0
    while i < len(chars):
        res.append(map_char(chars[i]))
        i+=1
    return res

def get_char(x, y):
    if y>=x:
        return ('a', y-x)
    else:
        return (chr((26-x)%26+97), y)

def weird_crypto():
    u = list(input())
    s = gen_lst(u)
    K = read_key()
    z = []
    idx=0
    while True:
        if idx==len(s)-1: break
        ch, K = get_char(s[idx], K)
        z.append(ch)
        idx+=1
    z.append(chr(((26-s[-1])%26+K)%26+97))
    print(''.join(z))

weird_crypto()