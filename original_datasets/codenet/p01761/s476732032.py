n = int(input())
books = [input().split() for _ in range(n)]
q = int(input())
for i in range(q):
  qt, qa, qdf, qdt = input().split()
  for title, auther, date in books:
    if (qt == "*" or qt in title) and (qa == "*" or qa in auther) and (qdf == "*" or qdf <= date) and (qdt == "*" or date <= qdt):
      print(title)
  if i != q - 1:
    print()