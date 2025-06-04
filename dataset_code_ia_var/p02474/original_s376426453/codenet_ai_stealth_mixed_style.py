def main():
    nums = input().split()
    def cast_to_int(vals):
        return [int(x) for x in vals]
    [first, second] = cast_to_int(nums)
    print(first * second)
main()