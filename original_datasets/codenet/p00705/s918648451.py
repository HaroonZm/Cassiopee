import collections
from operator import itemgetter

while True:
    max_value = 1
    num_people,num_border = map(int,raw_input().split())
    if (num_people == 0) and (num_border == 0):
        break
    list2 = []
    for i in range(num_people):
        line = raw_input()
        list1 = line.split()
        list1 = [int(s) for s in list1]
        if list1[0] != "0":
            del list1[0]
            list2.extend(list1)
    counter = collections.Counter(list2)
    if counter == {}:
        print "0"
    s = sorted(counter.items(), key=itemgetter(0))
    for key,value in sorted(s,key= itemgetter(1),reverse = True):
        if value >= num_border:
            print key
            break
        else:
            print "0"
            break