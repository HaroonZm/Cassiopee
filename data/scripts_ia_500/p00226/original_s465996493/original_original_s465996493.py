if __name__ == '__main__':

    while True:

        a,b = map(str,raw_input().split(' '))

        if a == '0' and b == '0':
            break

      #  print a,b

        a = list(a)
        b = list(b)
    #    print a

        br = 0
        hit = 0
        for i,data in enumerate(b):

            if data in a:
                if a[i] == data:
                    hit += 1

                else:
                    br += 1

        print hit,br