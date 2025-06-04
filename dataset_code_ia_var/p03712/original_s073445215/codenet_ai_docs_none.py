h,w=map(int,input().split())
a=[input() for _ in range(h)]
print('#'*(len(max(a))+2))
for s in a:
    print('#'+s+'#')
print('#'*(len(max(a))+2))