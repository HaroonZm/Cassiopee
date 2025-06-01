digit = [0, 1, 2, 3, 5, 7, 8, 9]
n = int(input())
while n != 0:
    new_num = []
    eight = 1
    while eight * 8 <= n:
        eight *= 8
    while eight > 0:
        new_num.append(n // eight)
        n %= eight
        eight //= 8
    nn_str = ''
    for i in range(len(new_num)):
        nn_str += str(digit[new_num[i]])
    print(nn_str)
    n = int(input())