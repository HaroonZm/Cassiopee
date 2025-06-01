def main():
    num_tasks, num_elements = map(int, input().split())
    task_workloads = [[] for _ in range(num_tasks)]
    while True:
        start_task, end_task, effort = map(int, input().split())
        if start_task == 0:
            break
        task_workloads[start_task - 1].append((end_task - 1, effort))

    num_queries = int(input())
    for _ in range(num_queries):
        factor_list = tuple(map(int, input().split()))
        total_efforts = [sum(factor_list[element] * effort for element, effort in task_workloads[task_index]) for task_index in range(num_tasks)]
        print(*total_efforts)

main()