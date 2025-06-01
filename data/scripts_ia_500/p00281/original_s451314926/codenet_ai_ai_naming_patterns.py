def main_function():
    number_of_workers, number_of_tasks = map(int, input().split())
    worker_task_effort_list = [[] for _ in range(number_of_workers + 1)]

    while True:
        start_worker, task_index, effort = map(int, input().split())
        if start_worker == 0:
            break
        worker_task_effort_list[start_worker].append((task_index - 1, effort))

    number_of_cases = int(input())
    for _ in range(number_of_cases):
        task_effort_tuple = tuple(map(int, input().split()))
        results_per_worker = [sum(task_effort_tuple[task] * effort for task, effort in worker_task_efforts) 
                              for worker_task_efforts in worker_task_effort_list[1:]]
        print(*results_per_worker)

main_function()