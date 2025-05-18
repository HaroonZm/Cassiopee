while 1:
      qua,bag = input().split()
      qua = int(qua)
      bag = int(bag)
      if qua == 0:
            break
      price = list(map(int,input().split()))
      price.sort(reverse=True)
      for i in range(qua):
            if (i+1)%bag == 0:
                  price[i]=-1
      for i in range(qua//bag):
            price.remove(-1)
      pay = sum(price)
      print(pay)