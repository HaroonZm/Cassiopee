initial_favorite_number, total_forbidden_numbers = tuple(map(int, input().split()))

forbidden_numbers_list = list(map(int, input().split()))

for difference_from_favorite in range(100):

    for direction in [-1, 1]:

        candidate_number = initial_favorite_number + difference_from_favorite * direction

        if candidate_number not in forbidden_numbers_list:

            print(candidate_number)

            exit(0)