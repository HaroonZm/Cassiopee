whos_there=lambda: int(input())
surprise=[*map(int,input().split())]
doorbell=0
current_index=1
while current_index<len(surprise):
    if (lambda prev,curr: prev<curr)(surprise[current_index-1],surprise[current_index]):
        doorbell+=1
    current_index+=1
print(doorbell)