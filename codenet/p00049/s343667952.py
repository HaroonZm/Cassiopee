dic = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}

while True:
    try:
        s = raw_input()
        sp = s.split(',')
        dic[ sp[1] ] += 1;
        
    except EOFError:
        print "%d\n%d\n%d\n%d" % (dic['A'], dic['B'], dic['AB'], dic['O'])
        break