import math

number_of_circle_pairs = int(input())

for _ in range(number_of_circle_pairs):
    
    x_center_a, y_center_a, radius_a, x_center_b, y_center_b, radius_b = map(float, input().split())
    
    centers_squared_distance = (x_center_a - x_center_b) ** 2 + (y_center_a - y_center_b) ** 2
    
    sum_of_radii_squared = (radius_a + radius_b) ** 2
    
    radius_difference_squared = (radius_a - radius_b) ** 2

    if centers_squared_distance <= sum_of_radii_squared:
        
        if radius_difference_squared > centers_squared_distance:
            
            if radius_a > radius_b:
                print(2)
            else:
                print(-2)
        
        else:
            print(1)
    
    else:
        print(0)