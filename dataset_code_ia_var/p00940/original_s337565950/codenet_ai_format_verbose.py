import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def solve():
    number_of_projects, number_of_resources, number_of_log_entries = map(int, input_stream().split())

    resources_available = list(map(int, input_stream().split()))
    resource_requirements_per_project = [ list(map(int, input_stream().split())) for _ in range(number_of_projects) ]
    log_entries = [ list(map(int, input().split())) for _ in range(number_of_log_entries) ]

    last_processed_log_index = -1

    current_resource_allocation = [ [0] * number_of_resources for _ in range(number_of_projects) ]

    def is_state_feasible(log_entry_index):

        nonlocal last_processed_log_index

        if last_processed_log_index < log_entry_index:
            for log_index in range(last_processed_log_index + 1, log_entry_index + 1):
                project_index, resource_index = log_entries[log_index]
                current_resource_allocation[project_index - 1][resource_index - 1] += 1
                resources_available[resource_index - 1] -= 1
        else:
            for log_index in range(log_entry_index + 1, last_processed_log_index + 1):
                project_index, resource_index = log_entries[log_index]
                current_resource_allocation[project_index - 1][resource_index - 1] -= 1
                resources_available[resource_index - 1] += 1

        available_resources_snapshot = resources_available[:]
        projects_completed = [0] * number_of_projects

        progress_made = True
        while progress_made:
            progress_made = False
            for project_index in range(number_of_projects):
                if projects_completed[project_index]:
                    continue

                can_complete_current_project = True
                for resource_index in range(number_of_resources):
                    resources_needed = resource_requirements_per_project[project_index][resource_index] - current_resource_allocation[project_index][resource_index]
                    if resources_needed > max(available_resources_snapshot[resource_index], 0):
                        can_complete_current_project = False
                        break

                if can_complete_current_project:
                    projects_completed[project_index] = 1
                    for resource_index in range(number_of_resources):
                        available_resources_snapshot[resource_index] += current_resource_allocation[project_index][resource_index]
                    progress_made = True

        last_processed_log_index = log_entry_index

        return sum(projects_completed) == number_of_projects

    search_left = 0
    search_right = number_of_log_entries

    while search_left + 1 < search_right:
        search_mid = (search_left + search_right) // 2
        if is_state_feasible(search_mid):
            search_left = search_mid
        else:
            search_right = search_mid

    if search_right == number_of_log_entries:
        output_stream("-1\n")
    else:
        output_stream(f"{search_right+1}\n")

solve()