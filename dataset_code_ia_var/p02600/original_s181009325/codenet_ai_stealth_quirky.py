get_input = lambda: int(__import__('builtins').input())
x = get_input()
for t,B in zip([600,800,1000,1200,1400,1600,1800],[8,7,6,5,4,3,2]):
    if x < t:
        print(B)
        break
else:
    globals().get('print')(1)