height, width = map(int, input().split())
min_area_difference = 0 if (height * width) % 3 == 0 else min(height, width)
if (height * width) % 3 != 0:
    for vertical_cut in range(1, width // 2 + 1):
        area_section1 = height * vertical_cut
        area_section2 = (width - vertical_cut) * (height // 2)
        area_section3 = (width - vertical_cut) * (height - height // 2)
        current_difference = max(area_section1, area_section2, area_section3) - min(area_section1, area_section2, area_section3)
        min_area_difference = min(min_area_difference, current_difference)
    for horizontal_cut in range(1, height // 2 + 1):
        area_section1 = width * horizontal_cut
        area_section2 = (height - horizontal_cut) * (width // 2)
        area_section3 = (height - horizontal_cut) * (width - width // 2)
        current_difference = max(area_section1, area_section2, area_section3) - min(area_section1, area_section2, area_section3)
        min_area_difference = min(min_area_difference, current_difference)
print(min_area_difference)