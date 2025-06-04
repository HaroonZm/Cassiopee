import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

grid_height, grid_width = map(int, input().split())
grid_contents = []
for i_row in range(grid_height):
    grid_contents.append(input())

def position_to_index(pos_row, pos_col):
    return pos_row * grid_width + pos_col

edge_start_list = []
edge_end_list = []
edge_weight_list = []
for cell_row in range(grid_height):
    for cell_col in range(grid_width):
        current_cell_index = position_to_index(cell_row, cell_col)
        if cell_row < grid_height - 1:
            neighbor_row = cell_row + 1
            neighbor_col = cell_col
            neighbor_index = position_to_index(neighbor_row, neighbor_col)
            weight = 0 if grid_contents[cell_row][cell_col] == grid_contents[neighbor_row][neighbor_col] else 1
            edge_start_list.append(current_cell_index)
            edge_end_list.append(neighbor_index)
            edge_weight_list.append(weight)
        if cell_col < grid_width - 1:
            neighbor_row = cell_row
            neighbor_col = cell_col + 1
            neighbor_index = position_to_index(neighbor_row, neighbor_col)
            weight = 0 if grid_contents[cell_row][cell_col] == grid_contents[neighbor_row][neighbor_col] else 1
            edge_start_list.append(current_cell_index)
            edge_end_list.append(neighbor_index)
            edge_weight_list.append(weight)

adjacency_matrix = csr_matrix((edge_weight_list, (edge_start_list, edge_end_list)), shape=(grid_height*grid_width, grid_height*grid_width))
shortest_distances = dijkstra(csgraph=adjacency_matrix, directed=True, indices=0)
destination_index = grid_height * grid_width - 1
result_distance = int(shortest_distances[destination_index])

start_cell = grid_contents[0][0]
end_cell = grid_contents[-1][-1]
if start_cell == '.' and end_cell == '.':
    print(result_distance // 2)
elif start_cell == '#' and end_cell == '#':
    print(result_distance // 2 + 1)
else:
    print(result_distance // 2 + 1)