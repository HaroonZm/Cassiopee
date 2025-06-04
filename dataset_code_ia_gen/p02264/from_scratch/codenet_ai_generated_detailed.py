from collections import deque
import sys

def round_robin_scheduling():
    # Read the number of processes (n) and the quantum time (q)
    n, q = map(int, sys.stdin.readline().split())
    
    # Initialize a queue to hold the processes
    # Each element is a tuple: (process_name, remaining_time)
    queue = deque()
    
    for _ in range(n):
        # Read each process name and its required time
        name, time = sys.stdin.readline().split()
        time = int(time)
        queue.append((name, time))
    
    # This will keep track of the current total elapsed time
    current_time = 0
    
    # List to store the output tuples (process_name, finish_time)
    finished_processes = []
    
    # Continue until all processes are completed
    while queue:
        # Take the first process from the queue
        name, time_left = queue.popleft()
        
        # If the process can finish within the quantum
        if time_left <= q:
            # Increase the current time by the time left for this process
            current_time += time_left
            # Process finished, record the finish time
            finished_processes.append((name, current_time))
        else:
            # Otherwise, use the quantum time slice
            current_time += q
            # Reduce the remaining time for the process
            time_left -= q
            # Put the process back at the end of the queue
            queue.append((name, time_left))
    
    # Print the results in the order processes finish
    for name, finish_time in finished_processes:
        print(name, finish_time)

# Run the scheduling simulation
if __name__ == "__main__":
    round_robin_scheduling()