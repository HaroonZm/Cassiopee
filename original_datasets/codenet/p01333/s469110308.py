def calculate1():
    change = B - A
    if change % 1000 == 0:
        one_thousand_count = change / 1000
        print_result(one_thousand_count)
    else:
        one_thousand_count = change / 1000
        remainder = change - one_thousand_count * 1000
        calculate2(remainder, one_thousand_count)
        
def calculate2(remainder, one_thousand_count):
    if remainder % 500 == 0:
        five_hundred_count = remainder / 500
        print_result(one_thousand_count, five_hundred_count)
    else:
        five_hundred_count = remainder / 500
        remainder = remainder - five_hundred_count * 500
        calculate3(remainder, one_thousand_count, five_hundred_count)
        
def calculate3(remainder, one_thousand_count, five_hundred_count):
        one_hundred_count = remainder / 100
        print_result(one_thousand_count, five_hundred_count, one_hundred_count)
        
def print_result(one_thousand_count=0, five_hundred_count=0, one_hundred_count=0):
    print '%s %s %s' % (one_hundred_count, five_hundred_count, one_thousand_count)

while True:
    A, B = map(int, raw_input().split())
    if A == 0 and B == 0: break
    calculate1()