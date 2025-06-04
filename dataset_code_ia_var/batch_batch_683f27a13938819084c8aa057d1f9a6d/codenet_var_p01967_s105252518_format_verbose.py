#!/usr/bin/env python

from collections import deque
import itertools as itertools_module
import sys
import math

sys.setrecursionlimit(1000000)

INFINITY_CONSTANT = 10 ** 18
MODULO_CONSTANT = 10 ** 9 + 7

number_of_resources = int(input())
resource_capacities = list(map(int, raw_input().split()))
current_resource_amounts = [0] * number_of_resources

number_of_queries = int(input())

for query_index in range(number_of_queries):
    command_type, resource_index, resource_delta = map(int, raw_input().split())
    
    if command_type == 1:
        current_resource_amounts[resource_index - 1] += resource_delta
    else:
        current_resource_amounts[resource_index - 1] -= resource_delta
    
    if not (0 <= current_resource_amounts[resource_index - 1] <= resource_capacities[resource_index - 1]):
        print(resource_index)
        exit()

print(0)