from bisect import bisect_right as bisect_right_bound
from itertools import accumulate

def main():
    
    number_of_books, number_of_shelves = map(int, input().split())
    
    books_weight_time_limits = [
        list(map(int, input().split()))
        for _ in range(number_of_books)
    ]
    
    prefix_sum_weights = list(
        accumulate([0] + [book[0] for book in books_weight_time_limits])
    )
    prefix_sum_times = list(
        accumulate([0] + [book[1] for book in books_weight_time_limits])
    )
    
    shelves_weight_time_capacity = [
        list(map(int, input().split()))
        for _ in range(number_of_shelves)
    ]
    
    memoization_dictionary = {}
    bitmask_full_shelves = (1 << number_of_shelves) - 1
    
    def get_last_placeable_book_index(starting_index, shelf_index):
        weight_capacity, time_capacity = shelves_weight_time_capacity[shelf_index]
        weight_limit_index = bisect_right_bound(
            prefix_sum_weights,
            prefix_sum_weights[starting_index] + weight_capacity
        )
        time_limit_index = bisect_right_bound(
            prefix_sum_times,
            prefix_sum_times[starting_index] + time_capacity
        )
        return min(weight_limit_index, time_limit_index) - 1
    
    def find_maximum_books(remaining_shelves_bitmask, memoization_dictionary):
        if remaining_shelves_bitmask in memoization_dictionary:
            return memoization_dictionary[remaining_shelves_bitmask]
        
        if remaining_shelves_bitmask == 0:
            return 0
        
        current_shelf_mask = 1
        maximum_books = 0
        
        for shelf_position in range(number_of_shelves):
            if remaining_shelves_bitmask & current_shelf_mask:
                previous_shelves_bitmask = remaining_shelves_bitmask & ~current_shelf_mask
                books_placed_before = find_maximum_books(previous_shelves_bitmask, memoization_dictionary)
                last_book_index = get_last_placeable_book_index(books_placed_before, shelf_position)
                maximum_books = max(maximum_books, last_book_index)
            current_shelf_mask <<= 1
        
        memoization_dictionary[remaining_shelves_bitmask] = maximum_books
        return maximum_books
    
    print(find_maximum_books(bitmask_full_shelves, memoization_dictionary))
    
main()