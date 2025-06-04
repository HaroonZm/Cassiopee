import sys

def largest_rectangle(heights):
    n = len(heights)
    max_area = 0

    for i in range(n):
        height = heights[i]
        left = i
        right = i

        # Move left pointer to the leftmost index where height >= heights[i]
        while left > 0 and heights[left - 1] >= height:
            left -= 1

        # Move right pointer to the rightmost index where height >= heights[i]
        while right < n - 1 and heights[right + 1] >= height:
            right += 1

        width = right - left + 1
        area = height * width

        if area > max_area:
            max_area = area

    return max_area

def main(args):
    _ = input()
    nums = input()
    heights = list(map(int, nums.split()))
    answer = largest_rectangle(heights)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])