ThatNumber = int(input())
sss = [word for word in input().split()]
unique_colors = {c for c in sss}
match len(unique_colors):
    case 3:
        print("Three")
    case _:
        print("Four")