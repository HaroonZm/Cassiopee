from collections import deque

class MaxHeapPriorityQueue:
    def __init__(self, maximum_capacity):
        self.heap_storage = [None] * maximum_capacity
        self.current_number_of_elements = 0

    def insert(self, job_tuple):
        current_index = self.current_number_of_elements
        self.current_number_of_elements += 1
        self.heap_storage[current_index] = job_tuple

        while current_index != 0:
            parent_index = (current_index - 1) // 2
            if self.heap_storage[parent_index][1] < self.heap_storage[current_index][1]:
                self.heap_storage[parent_index], self.heap_storage[current_index] = (
                    self.heap_storage[current_index],
                    self.heap_storage[parent_index],
                )
                current_index = parent_index
            else:
                return

    def get_max(self):
        return self.heap_storage[0]

    def get_current_size(self):
        return self.current_number_of_elements

    def remove_max(self):
        max_value = self.heap_storage[0]
        self.heap_storage[0] = self.heap_storage[self.current_number_of_elements - 1]
        self.current_number_of_elements -= 1
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            if left_child_index >= self.current_number_of_elements:
                return max_value
            right_child_index = 2 * current_index + 2
            if right_child_index >= self.current_number_of_elements:
                right_child_index = left_child_index

            if (
                self.heap_storage[current_index][1] > self.heap_storage[left_child_index][1]
                and self.heap_storage[current_index][1] > self.heap_storage[right_child_index][1]
            ):
                return max_value
            elif self.heap_storage[left_child_index][1] > self.heap_storage[right_child_index][1]:
                self.heap_storage[current_index], self.heap_storage[left_child_index] = (
                    self.heap_storage[left_child_index],
                    self.heap_storage[current_index],
                )
                current_index = left_child_index
            else:
                self.heap_storage[current_index], self.heap_storage[right_child_index] = (
                    self.heap_storage[right_child_index],
                    self.heap_storage[current_index],
                )
                current_index = right_child_index
        return max_value

def get_maximum_total_reward(number_of_jobs, total_days, job_deadlines, job_rewards):
    maximum_total_reward = 0
    
    jobs_sorted_by_deadline = deque(
        sorted(zip(job_deadlines, job_rewards), key=lambda job: job[0])
    )
    
    available_jobs_priority_queue = MaxHeapPriorityQueue(number_of_jobs)

    for current_day in range(1, total_days + 1):
        while jobs_sorted_by_deadline and jobs_sorted_by_deadline[0][0] == current_day:
            job_to_add = jobs_sorted_by_deadline.popleft()
            available_jobs_priority_queue.insert(job_to_add)
        
        if available_jobs_priority_queue.get_current_size() > 0:
            most_rewarding_job = available_jobs_priority_queue.remove_max()
            maximum_total_reward += most_rewarding_job[1]

    return maximum_total_reward

if __name__ == '__main__':
    number_of_jobs, total_days = map(int, input().split())
    job_deadlines = [0] * number_of_jobs
    job_rewards = [0] * number_of_jobs

    for job_index in range(number_of_jobs):
        job_deadlines[job_index], job_rewards[job_index] = map(int, input().split())

    final_maximum_reward = get_maximum_total_reward(
        number_of_jobs,
        total_days,
        job_deadlines,
        job_rewards
    )

    print(final_maximum_reward)