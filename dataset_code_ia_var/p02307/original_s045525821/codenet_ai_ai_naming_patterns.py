from decimal import Decimal

coord1_x_str, coord1_y_str = map(str, input().split())
coord2_x_str, coord2_y_str = map(str, input().split())
coord3_x_str, coord3_y_str = map(str, input().split())

coord1_x = Decimal(coord1_x_str)
coord1_y = Decimal(coord1_y_str)
coord2_x = Decimal(coord2_x_str)
coord2_y = Decimal(coord2_y_str)
coord3_x = Decimal(coord3_x_str)
coord3_y = Decimal(coord3_y_str)

side_12_len = ((coord1_x - coord2_x) ** Decimal('2') + (coord1_y - coord2_y) ** Decimal('2')) ** Decimal('0.5')
side_23_len = ((coord3_x - coord2_x) ** Decimal('2') + (coord3_y - coord2_y) ** Decimal('2')) ** Decimal('0.5')
side_13_len = ((coord1_x - coord3_x) ** Decimal('2') + (coord1_y - coord3_y) ** Decimal('2')) ** Decimal('0.5')

semi_perimeter = (side_12_len + side_23_len + side_13_len) / Decimal('2')

circum_radius = (side_12_len * side_23_len * side_13_len) / ((semi_perimeter * (semi_perimeter - side_12_len) * (semi_perimeter - side_23_len) * (semi_perimeter - side_13_len)) ** Decimal('0.5') * Decimal('4'))

midpoint_12_x = (coord1_x + coord2_x) / 2
midpoint_12_y = (coord1_y + coord2_y) / 2
midpoint_23_x = (coord3_x + coord2_x) / 2
midpoint_23_y = (coord3_y + coord2_y) / 2

if (coord3_y - coord2_y) != 0 and (coord2_y - coord1_y) != 0:
    perp_slope_23 = -(coord3_x - coord2_x) / (coord3_y - coord2_y)
    perp_intercept_23 = ((coord3_x - coord2_x) * midpoint_23_x + (coord3_y - coord2_y) * midpoint_23_y) / (coord3_y - coord2_y)
    perp_slope_12 = -(coord2_x - coord1_x) / (coord2_y - coord1_y)
    perp_intercept_12 = ((coord2_x - coord1_x) * midpoint_12_x + (coord2_y - coord1_y) * midpoint_12_y) / (coord2_y - coord1_y)
    circumcenter_x = (perp_intercept_12 - perp_intercept_23) / (perp_slope_23 - perp_slope_12)
    circumcenter_y = perp_slope_23 * circumcenter_x + perp_intercept_23

if coord3_y - coord2_y == 0:
    circumcenter_x = midpoint_23_x
    perp_slope_12 = -(coord2_x - coord1_x) / (coord2_y - coord1_y)
    perp_intercept_12 = ((coord2_x - coord1_x) * midpoint_12_x + (coord2_y - coord1_y) * midpoint_12_y) / (coord2_y - coord1_y)
    circumcenter_y = perp_slope_12 * circumcenter_x + perp_intercept_12

if coord2_y - coord1_y == 0:
    circumcenter_x = midpoint_12_x
    perp_slope_23 = -(coord3_x - coord2_x) / (coord3_y - coord2_y)
    perp_intercept_23 = ((coord3_x - coord2_x) * midpoint_23_x + (coord3_y - coord2_y) * midpoint_23_y) / (coord3_y - coord2_y)
    circumcenter_y = perp_slope_23 * circumcenter_x + perp_intercept_23

print(circumcenter_x, circumcenter_y, circum_radius)