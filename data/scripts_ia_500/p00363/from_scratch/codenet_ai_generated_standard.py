W, H, c = input().split()
W, H = int(W), int(H)
print('+' + '-'*(W-2) + '+')
for i in range(1, H-1):
    if i == (H-1)//2:
        print('|' + '.'*((W-1)//2) + c + '.'*((W-1)//2) + '|')
    else:
        print('|' + '.'*(W-2) + '|')
print('+' + '-'*(W-2) + '+')