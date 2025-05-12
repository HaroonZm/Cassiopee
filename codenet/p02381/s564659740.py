n = int(input())

while n != 0:
    test = [int(x) for x in input().split()]
    
    ave_test = sum(test)/n
    
    total_test = 0
    for i in range(n):
        sum_test = (test[i] - ave_test)**2
        #print(sum_test)
        total_test += sum_test
    sd_test = (total_test/n)**0.5
    print(sd_test)
    n = int(input())