import sys

def compute_salaries(employee_count, task_count, employee_logs, task_prices):
    employee_expenses = [dict() for _ in range(employee_count + 1)]
    for employee_id, task_id, effort in employee_logs:
        employee_expenses[employee_id][task_id] = employee_expenses[employee_id].get(task_id, 0) + effort
    return [
        sum(task_prices[task_id - 1] * effort for task_id, effort in expenses.items())
        for expenses in employee_expenses[1:]
    ]

def main(args):
    number_of_employees, number_of_tasks = map(int, input().split())
    logs = []
    while True:
        emp_id, task_id, effort = map(int, input().split())
        if emp_id == 0 and task_id == 0 and effort == 0:
            break
        logs.append((emp_id, task_id, effort))
    prices = [int(p) for p in input().split()]
    repetition_count = int(input())
    for _ in range(repetition_count):
        results = compute_salaries(number_of_employees, number_of_tasks, logs, prices)
        print(*results, sep=' ')

if __name__ == '__main__':
    main(sys.argv[1:])