def read_number():
    return int(input())

def read_movie_input():
    a, b = map(int, input().split())
    return a, b

def adjust_day(day):
    return day - 1

def init_movie_lists(count):
    return [], []

def init_movies_per_day(days):
    return [[] for _ in range(days)]

def add_movie_period(a, b, n, movies_by_day):
    for day in range(a, b + 1):
        movies_by_day[day].append(n)

def get_unseen_movies(movies_today, picked):
    return [m for m in movies_today if not picked[m]]

def is_empty(lst):
    return len(lst) == 0

def pick_movie_with_earliest_end(unseen, Bs):
    lastday = float('inf')
    should_see = -1
    for m in unseen:
        if Bs[m] < lastday:
            lastday = Bs[m]
            should_see = m
    return should_see

def mark_movie_as_picked(picked, index):
    picked[index] = True

def add_ticket_reward(ans, reward):
    return ans + reward

def process_day(day, movies, picked, Bs):
    unseen = get_unseen_movies(movies, picked)
    if is_empty(unseen):
        reward = 50
    else:
        to_see = pick_movie_with_earliest_end(unseen, Bs)
        mark_movie_as_picked(picked, to_see)
        reward = 100
    return reward

def main():
    N = read_number()
    As, Bs = init_movie_lists(N)
    days_in_month = 31
    movies_by_day = init_movies_per_day(days_in_month)
    for n in range(N):
        a, b = read_movie_input()
        a = adjust_day(a)
        b = adjust_day(b)
        As.append(a)
        Bs.append(b)
        add_movie_period(a, b, n, movies_by_day)
    picked = [False] * N
    ans = 0
    for day in range(days_in_month):
        reward = process_day(day, movies_by_day[day], picked, Bs)
        ans = add_ticket_reward(ans, reward)
    print(ans)

main()