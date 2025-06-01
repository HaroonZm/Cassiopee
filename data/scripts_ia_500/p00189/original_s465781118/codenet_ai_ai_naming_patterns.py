import sys
from sys import stdin
input = stdin.readline

def floyd_warshall(num_vertices, dist_matrix):
    for intermediate_vertex in range(num_vertices):
        for start_vertex in range(num_vertices):
            dist_start_intermediate = dist_matrix[start_vertex][intermediate_vertex]
            for end_vertex in range(num_vertices):
                dist_intermediate_end = dist_matrix[intermediate_vertex][end_vertex]
                if dist_matrix[start_vertex][end_vertex] > dist_start_intermediate + dist_intermediate_end:
                    dist_matrix[start_vertex][end_vertex] = dist_start_intermediate + dist_intermediate_end

def main(args):
    MAX_TOWN_LIMIT = 10
    while True:
        edge_count = int(input())
        if edge_count == 0:
            break
        distance_matrix = [[float('inf')] * MAX_TOWN_LIMIT for _ in range(MAX_TOWN_LIMIT)]
        for vertex_index in range(MAX_TOWN_LIMIT):
            distance_matrix[vertex_index][vertex_index] = 0

        highest_town_index = 0
        for _ in range(edge_count):
            town_from, town_to, cost = map(int, input().split())
            distance_matrix[town_from][town_to] = cost
            distance_matrix[town_to][town_from] = cost
            highest_town_index = max(highest_town_index, town_from, town_to)

        floyd_warshall(highest_town_index + 1, distance_matrix)

        minimum_total_distance = float('inf')
        town_with_min_distance = -1
        for town_index, dist_row in enumerate(distance_matrix[:highest_town_index + 1]):
            total_distance = sum(dist_row[:highest_town_index + 1])
            if total_distance < minimum_total_distance:
                minimum_total_distance = total_distance
                town_with_min_distance = town_index

        print(f'{town_with_min_distance} {minimum_total_distance}')

if __name__ == '__main__':
    main(sys.argv[1:])