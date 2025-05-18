Cards = [int(x) for x in input().split()]
Cards.sort(reverse=True)
ans = Cards[0] * 10 + Cards[1] + Cards[2]
print(ans)