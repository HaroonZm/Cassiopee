d=lambda s:7-(["MON","TUE","WED","THU","FRI","SAT","SUN"].index(s) if s in ["MON","TUE","WED","THU","FRI","SAT","SUN"] else 0)
print((lambda f: f(input()))(d))