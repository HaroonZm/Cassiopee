N = int(input())
dic = {}
i = 0
while i < N:
    a = int(input())
    dic[i+1] = a
    i += 1
counter = 0
place = 1
while place != 2:
    if place in dic:
        if dic[place] in dic:
            if dic[place] != place:
                temp = dic[place]
                dic.pop(place)
                place = temp
                counter += 1
            else:
                counter = -1
                break
        else:
            counter = -1
            break
    else:
        counter = -1
        break
print(counter)