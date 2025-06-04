def_coord_height, def_coord_width = map(int, input().split())
blk_coords_list = []
for iter_height in range(def_coord_height):
    input_line = input()
    for iter_width in range(def_coord_width):
        if input_line[iter_width] == "B":
            blk_coords_list.append([iter_height, iter_width])

boundary_lu = [def_coord_height + def_coord_width, 0]
boundary_ld = [def_coord_height + def_coord_width, 0]
for blk_height, blk_width in blk_coords_list:
    boundary_lu = [min(boundary_lu[0], blk_height + blk_width), max(boundary_lu[1], blk_height + blk_width)]
    boundary_ld = [min(boundary_ld[0], def_coord_height - blk_height + blk_width), max(boundary_ld[1], def_coord_height - blk_height + blk_width)]
print(max(boundary_lu[1] - boundary_lu[0], boundary_ld[1] - boundary_ld[0]))