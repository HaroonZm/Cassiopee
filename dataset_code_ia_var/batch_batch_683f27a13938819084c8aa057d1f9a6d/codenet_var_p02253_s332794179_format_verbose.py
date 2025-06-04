number_of_activities = int(input())

activities = [ [int(activity_detail) for activity_detail in input().split()] for _ in range(number_of_activities) ]

activities.sort(key = lambda activity : activity[1])

current_end_time = 0

selected_activities_count = 0

for activity in activities:
    
    activity_start_time = activity[0]
    activity_end_time = activity[1]
    
    if current_end_time < activity_start_time:
        selected_activities_count += 1
        current_end_time = activity_end_time

print(selected_activities_count)