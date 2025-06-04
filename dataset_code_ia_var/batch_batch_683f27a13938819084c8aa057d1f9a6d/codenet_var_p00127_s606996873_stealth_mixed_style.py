table = dict([(11,'a'),(12,'b'),(13,'c'),(14,'d'),(15,'e'),
              (21,'f'),(22,'g'),(23,'h'),(24,'i'),(25,'j'),
              (31,'k'),(32,'l'),(33,'m'),(34,'n'),(35,'o'),
              (41,'p'),(42,'q'),(43,'r'),(44,'s'),(45,'t'),
              (51,'u'),(52,'v'),(53,'w'),(54,'x'),(55,'y'),
              (61,'z'),(62,'.'),(63,'?'),(64,'!'),(65,' ')])

def decode(s):
    i = 0
    res = ''
    while i < len(s):
        k = int(s[i]+s[i+1]) if i+1 < len(s) else -1
        res += table[k] if k in table else 'NA'
        i += 2
    return res

go = True
while go:
    try:
        s = input()
        out = (lambda x: print('NA') if 'NA' in x else print(x))(decode(s))
    except:
        go = False