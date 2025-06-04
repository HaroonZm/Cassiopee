W, H, c = input().split()
W, H = int(W), int(H)
print('+' + '-'*(W-2) + '+')
for i in range(H-2):
    if i == (H-2)//2:
        print('|' + '.'*((W-3)//2) + c + '.'*((W-3)//2) + '|')
    else:
        print('|' + '.'*(W-2) + '|')
print('+' + '-'*(W-2) + '+')