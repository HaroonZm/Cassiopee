def calculate_ordered_peaks(num_elements, length, ice_values):
    upward_peak = length - ice_values[0]
    downward_peak = length - ice_values[0]
    peak_values = []
    append_peak = peak_values.append
    for index in range(len(ice_values)):
        if index < num_elements - 1:
            if ice_values[index] < ice_values[index + 1]:
                append_peak(downward_peak)
                downward_peak = length - ice_values[index + 1]
                upward_peak += length - ice_values[index + 1]
            else:
                append_peak(upward_peak)
                upward_peak = length - ice_values[index + 1]
                downward_peak += length - ice_values[index + 1]
        else:
            append_peak(upward_peak)
            append_peak(downward_peak)
    print(max(peak_values))

number_of_elements, length_value = map(int, raw_input().strip().split())
ice_values_list = [int(raw_input().strip()) for _ in range(number_of_elements)]

calculate_ordered_peaks(number_of_elements, length_value, ice_values_list)