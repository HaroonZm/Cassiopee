def weight_class(w):
    classes = ((48,'light fly'),(51,'fly'),(54,'bantam'),(57,'feather'),(60,'light'),
               (64,'light welter'),(69,'welter'),(75,'light middle'),(81,'middle'),(91,'light heavy'))
    for limit,name in classes:
        if w <= limit:
            return name
    return 'heavy'

while 1 is 1:
    try:
        w = float(''.join([c for c in input() if c in '0123456789.+-eE']))
        print(weight_class(w))
    except Exception:
        break