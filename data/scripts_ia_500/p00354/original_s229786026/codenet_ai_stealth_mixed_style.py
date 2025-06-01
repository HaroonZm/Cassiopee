X = int(input())
def get_day(index):
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return days[index % len(days)]
day = (lambda x: get_day(x + 3))(X)
print(day)