import heapq

def main():
    """
    Main function to solve the priority queue problem.

    It reads the number of items (N) and number of operations (M),
    then processes M times to halve the highest value in a list, using a max-heap.
    Finally, prints the sum of the resulting numbers.
    """

    # Read number of elements N and number of operations M from standard input
    N, M = map(int, input().split())
    
    # Read the list of integers from standard input and convert to max-heap by negating values,
    # since heapq in Python implements a min-heap
    A = list(map(lambda x: int(x)*(-1), input().split()))
    
    # Transform the list into a heap in-place
    heapq.heapify(A)

    # Perform M operations; each time, replace the largest element with its half (rounded down)
    for _ in range(M):
        # Remove the largest element (smallest negative number)
        num = heapq.heappop(A)
        # Halve the extracted value and re-negate appropriately to maintain max-heap property.
        # Use (-num)//2*(-1) to get the next value (half, as negative, re-negated).
        new_num = (-num) // 2 * (-1)
        # Insert the new value back into the heap
        heapq.heappush(A, new_num)
    
    # Calculate the sum of the current state of the heap.
    # Negate the sum to revert back to the original sign.
    result = sum(A) * (-1)
    print(result)

if __name__ == "__main__":
    main()