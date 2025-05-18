import math
a,b,c,d=map(int,input().split())
ans=""
for i in range (c-a):
    ans+="R"
for i in range (d-b):
    ans+="U"
for i in range (c-a):
    ans+="L"
for i in range (d-b):
    ans+="D"
ans+="D"
for i in range (c-a+1):
    ans+="R"
for i in range (d-b+1):
    ans+="U"
ans+="LU"
for i in range (c-a+1):
    ans+="L"
for i in range (d-b+1):
    ans+="D"
ans+="R"
print(ans)