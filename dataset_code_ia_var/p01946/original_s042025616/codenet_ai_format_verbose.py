start_health, target_health, duration = map(int, input().split())

required_health = start_health - target_health

health_changes_per_period = list(map(int, input().split()))

total_health_change_per_cycle = sum(health_changes_per_period)

if total_health_change_per_cycle >= 0:
    
    current_health = required_health
    
    for period_index, health_change_in_period in enumerate(health_changes_per_period):
        
        current_health += health_change_in_period
        
        if current_health <= 0:
            
            print(period_index + 1)
            break
            
    else:
        print(-1)
    
    exit(0)

minimum_cumulative_health = 0
cumulative_health = 0

for health_change_in_period in health_changes_per_period:
    cumulative_health += health_change_in_period
    minimum_cumulative_health = min(minimum_cumulative_health, cumulative_health)

number_of_full_cycles = max((required_health + minimum_cumulative_health - total_health_change_per_cycle - 1) // (-total_health_change_per_cycle), 0)

required_health += number_of_full_cycles * total_health_change_per_cycle

for period_index, health_change_in_period in enumerate(health_changes_per_period):
    required_health += health_change_in_period
    if required_health <= 0:
        print(period_index + 1 + number_of_full_cycles * duration)
        break
else:
    assert False