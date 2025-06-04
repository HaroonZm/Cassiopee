get_num = lambda: int(input())
get_list = lambda: [int(x) for x in input().split()]
num = get_num()
values = get_list()
result = sum([(values[i] == i+1) and ((result:=result+1) or True) and not (reset:=False) if (flag:=not i or not reset) else False for i in range(num) if not (reset:=values[i]==i+1)])
print(result)