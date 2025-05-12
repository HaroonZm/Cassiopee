def main():
    stop = list(input())

    a, b = 0, 0
    for i in stop:
        if 'A' == i:
            a+=1
        else:
            b+=1
    if a > 0 and b > 0:
        print('Yes')
    else:
        print('No')
main()