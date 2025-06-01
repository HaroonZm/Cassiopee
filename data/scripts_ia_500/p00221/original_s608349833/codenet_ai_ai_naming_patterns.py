import sys
from sys import stdin
from collections import deque

input_line_reader = stdin.readline

def fizzbuzz_generator(start_value=1):
    current_number = start_value
    while True:
        if current_number % 15 == 0:
            output_value = 'FizzBuzz'
        elif current_number % 5 == 0:
            output_value = 'Buzz'
        elif current_number % 3 == 0:
            output_value = 'Fizz'
        else:
            output_value = str(current_number)
        yield output_value
        current_number += 1

def main_function(argv):
    while True:
        count_players, num_rounds = map(int, input_line_reader().split())
        if count_players == 0 and num_rounds == 0:
            break
        players_queue = deque(range(1, count_players + 1))
        fizzbuzz_iter = fizzbuzz_generator()
        for _ in range(num_rounds):
            player_response = input_line_reader().strip()
            correct_response = next(fizzbuzz_iter)
            if player_response != correct_response:
                if len(players_queue) > 1:
                    players_queue.popleft()
            else:
                players_queue.rotate(-1)
        surviving_players = sorted(players_queue)
        print(*surviving_players)

if __name__ == '__main__':
    main_function(sys.argv[1:])