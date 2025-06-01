while True:
    number_of_cuts = int(input())
    if number_of_cuts == 0:
        break
    slice_sizes = list(map(int, input().split()))
    total_cake_size = sum(slice_sizes)
    number_of_friends = number_of_cuts - 1
    slice_per_friend = total_cake_size // number_of_friends
    print(slice_per_friend)