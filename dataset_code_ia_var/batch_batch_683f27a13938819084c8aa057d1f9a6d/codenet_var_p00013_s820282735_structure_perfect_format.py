list1 = []
for i in range(1, 200):
    try:
        str1 = input()
        if str1 != '0' and str1 != '':
            list1.append(str1)
        elif str1 == '0':
            print(list1.pop())
        else:
            break
    except:
        break