x = int(input())
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def get_day(index):
    return days[(index + 3) % len(days)]

print(get_day(x))