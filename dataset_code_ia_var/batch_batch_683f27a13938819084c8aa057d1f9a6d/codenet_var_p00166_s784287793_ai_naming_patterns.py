from math import sin, pi

def calculate_partition_sum(angle_list):
    return sum([(sin(angle_value * pi / 180) / 2) for angle_value in angle_list])

while True:
    partition1_count = input()
    if partition1_count == 0:
        break
    partition1_angles = [int(raw_input()) for partition1_index in range(partition1_count - 1)]
    partition1_angles.append(360 - sum(partition1_angles))
    
    partition2_count = input()
    partition2_angles = [int(raw_input()) for partition2_index in range(partition2_count - 1)]
    partition2_angles.append(360 - sum(partition2_angles))
    
    partition1_sum = calculate_partition_sum(partition1_angles)
    partition2_sum = calculate_partition_sum(partition2_angles)
    
    if partition1_sum - partition2_sum > 1e-10:
        print 1
    elif partition2_sum - partition1_sum > 1e-10:
        print 2
    else:
        print 0