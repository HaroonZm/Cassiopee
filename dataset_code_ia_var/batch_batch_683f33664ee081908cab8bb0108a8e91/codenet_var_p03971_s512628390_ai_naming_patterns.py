def process_applicants():
    input_candidate_count, input_quota_a, input_quota_b = [int(input_value) for input_value in input().split()]
    input_applicant_types = input()
    accepted_count_a, accepted_count_b = 0, 0
    acceptance_results = ['No'] * input_candidate_count
    for applicant_index in range(input_candidate_count):
        applicant_type = input_applicant_types[applicant_index]
        if applicant_type == 'c':
            continue
        if applicant_type == 'a':
            if accepted_count_a + accepted_count_b < input_quota_a + input_quota_b:
                acceptance_results[applicant_index] = 'Yes'
                accepted_count_a += 1
        if applicant_type == 'b':
            if accepted_count_a + accepted_count_b < input_quota_a + input_quota_b and accepted_count_b < input_quota_b:
                acceptance_results[applicant_index] = 'Yes'
                accepted_count_b += 1
    for acceptance_status in acceptance_results:
        print(acceptance_status)

if __name__ == "__main__":
    process_applicants()