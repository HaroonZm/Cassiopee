initial_amount, total_time, total_resource = map(int, input().split())

resource_rate_per_unit = total_resource / initial_amount

accumulated_resource = resource_rate_per_unit * total_time

print(accumulated_resource)