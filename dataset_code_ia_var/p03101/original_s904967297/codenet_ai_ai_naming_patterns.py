height_total, width_total = map(int, input().split())
height_cut, width_cut = map(int, input().split())

remaining_height = height_total - height_cut
remaining_width = width_total - width_cut

area_remaining = remaining_height * remaining_width

print(area_remaining)