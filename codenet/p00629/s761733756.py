while 1:
    in_tmp = input()
    if (in_tmp == "0"):
        break
    list_team = []
    for i in range(int(in_tmp)):
        list_team.append(list(map(int,input().split())))
    list_sorted = sorted(list_team, key=lambda x:(-x[2], x[3], x[0]))
    
    cnt_passed = 0
    dict_passed = {}
    for item in list_sorted:
        if (item[1] not in dict_passed.keys()):
            dict_passed[item[1]] = 0
        if (cnt_passed < 10):
            if(dict_passed[item[1]] < 3):
                print(item[0])
                dict_passed[item[1]] += 1
                cnt_passed += 1
        elif (cnt_passed < 20):
            if(dict_passed[item[1]] < 2):
                print(item[0])
                dict_passed[item[1]] += 1
                cnt_passed += 1
        elif (cnt_passed < 26):
            if(dict_passed[item[1]] < 1):
                print(item[0])
                dict_passed[item[1]] += 1
                cnt_passed += 1
        else:
            break