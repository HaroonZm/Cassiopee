#文字列を取得する
strings = list(input())

#for文で奇数番目を取り出す
for number in range(len(strings)):
  if number % 2 == 0:
    #改行なしにする
    print(strings[number], end ="")