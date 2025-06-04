table=lambda: {11:'a',12:'b',13:'c',14:'d',15:'e',
               21:'f',22:'g',23:'h',24:'i',25:'j',
               31:'k',32:'l',33:'m',34:'n',35:'o',
               41:'p',42:'q',43:'r',44:'s',45:'t',
               51:'u',52:'v',53:'w',54:'x',55:'y',
               61:'z',62:'.',63:'?',64:'!',65:' '}
dic = table()

def decode(msg:str) -> str:
    res = []
    for index in range(0,len(msg),2):
        try:
            key = int(msg[index:index+2])
            res.append(dic.get(key,'NA'))
        except ValueError:
            return 'NA'
    if 'NA' in res:
        return 'NA'
    return ''.join(res)

print("\nEnter code (empty to quit):")
while 1:
    raw = input()
    if not raw: break
    out = decode(raw)
    print(out)