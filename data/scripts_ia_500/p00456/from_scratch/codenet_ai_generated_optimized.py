w=[int(input())for _ in range(10)]
k=[int(input())for _ in range(10)]
print(sum(sorted(w,reverse=True)[:3]),sum(sorted(k,reverse=True)[:3]))