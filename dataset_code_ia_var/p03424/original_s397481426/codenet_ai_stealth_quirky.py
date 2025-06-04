n=int(input())
s=[*input().split()]

def unconventional(lst):
    try:
        next(i for i in lst if i=="Y")
        print("Four")
    except StopIteration:
        print("Three")

unconventional(list({*s}))