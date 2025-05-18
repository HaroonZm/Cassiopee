from collections import Counter
def parse_card(card):
  suit = card[-1]
  num = card[:-1]
  if num == "A":num = 1
  elif num == "K":num = 13
  elif num == "Q":num = 12
  elif num == "J":num = 11
  elif num == "T":num = 10
  else:num = int(num)
  return (num, suit)
  
def parse_hand(hand):
  return sorted((map(parse_card, hand)))

def judge(hand):
  nums = [num for num, _ in hand]
  flash_flag = len({suit for _, suit in hand}) == 1
  head = nums[0]
  straight_flag = [head, head + 1, head + 2, head + 3, head + 4] == nums or \
                  [1, 10, 11, 12, 13] == nums
  dist = sorted(Counter(nums).values())
  
  if nums == [1, 10, 11, 12, 13] and flash_flag:return 9
  if straight_flag and flash_flag:return 8
  if dist == [1, 4]:return 7
  if dist == [2, 3]:return 6
  if flash_flag:return 5
  if straight_flag:return 4
  if dist == [1, 1, 3]:return 3
  if dist == [1, 2, 2]:return 2
  if dist == [1, 1, 1, 2]:return 1
  else:return 0

def score(hand, dic, point):
  ret = 0
  for num, suit in hand:
    ret += dic[suit][num - 1]
  ret *= point[judge(hand)]
  return ret

def main():
  first_flag = True
  while True:
    try:
      n = int(input())
    except EOFError:
      break
    
    if not first_flag:print()
    else:first_flag = False
    
    dic = {}
    dic["S"] = list(map(int, input().split()))
    dic["C"] = list(map(int, input().split()))
    dic["H"] = list(map(int, input().split()))
    dic["D"] = list(map(int, input().split()))
    point = [0] + list(map(int, input().split()))
    for _ in range(n):
      hand = parse_hand(input().split())
      print(score(hand, dic, point))

main()