list1 = []
i = 1
while i < 200:
    try:
        str1 = input()
        if str1 != '0' and str1 != '':
            list1.append(str1)
        elif str1 == '0':
            if len(list1) > 0:
                print(list1.pop())
            else:
                print("La liste est vide")
        else:
            break
        i += 1
    except:
        break