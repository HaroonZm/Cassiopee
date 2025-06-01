def solve():
    
    import sys
    from collections import deque
    
    input_stream = sys.stdin
    
    number_of_students, number_of_shuffles, number_of_queries = map(int, input_stream.readline().split())
    
    students_queue = deque(range(number_of_students))
    exemption_status = [1] * number_of_students
    
    shuffle_values = map(int, input_stream.readline().split())
    
    for shuffle_value in shuffle_values:
        
        if shuffle_value % 2 == 1:
            students_queue.rotate(shuffle_value)
        else:
            students_queue.rotate(-shuffle_value)
        
        removed_student = students_queue.popleft()
        exemption_status[removed_student] = 0
    
    query_students = map(int, input_stream.readline().split())
    
    for student_index in query_students:
        print(exemption_status[student_index])

solve()