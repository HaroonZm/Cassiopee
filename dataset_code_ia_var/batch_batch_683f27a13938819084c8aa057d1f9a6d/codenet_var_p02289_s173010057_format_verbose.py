import heapq
import sys

read_input = sys.stdin.readline

max_heap = []

while True:
    user_input = read_input()
    
    if user_input[0] == "e" and user_input[1] == "n":
        exit()
    elif user_input[0] == "e":
        largest_value = -heapq.heappop(max_heap)
        print(largest_value)
    else:
        command, number_string = user_input.split()
        number_value = int(number_string)
        heapq.heappush(max_heap, -number_value)