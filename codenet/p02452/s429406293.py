"""
Binary Search - Includes
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_6_B&lang=jp

"""
_ = input()
A = set(input().split())
_ = input()
B = set(input().split())
print(int(A & B == B))