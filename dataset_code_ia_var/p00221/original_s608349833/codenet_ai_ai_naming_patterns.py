import sys
from sys import stdin
from collections import deque

def fizzbuzz_generator(iteration_start=1):
    current = iteration_start
    while True:
        if current % 15 == 0:
            yield 'FizzBuzz'
        elif current % 5 == 0:
            yield 'Buzz'
        elif current % 3 == 0:
            yield 'Fizz'
        else:
            yield str(current)
        current += 1

def process_game(input_args):
    input_reader = stdin.readline
    while True:
        player_count, round_count = map(int, input_reader().split())
        if player_count == 0 and round_count == 0:
            break
        active_players = deque(range(1, player_count + 1))
        fizzbuzz_iter = fizzbuzz_generator()
        for _ in range(round_count):
            current_response = input_reader().strip()
            expected_response = next(fizzbuzz_iter)
            if current_response != expected_response:
                if len(active_players) > 1:
                    active_players.popleft()
            else:
                active_players.rotate(-1)
        surviving_players = list(active_players)
        surviving_players.sort()
        print(*surviving_players)

if __name__ == '__main__':
    process_game(sys.argv[1:])