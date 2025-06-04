def get_min_max():
    nums = []
    for n in input().split():
        nums.append(int(n))
    class Helper:
        @staticmethod
        def mini(l):
            m = l[0]
            for i in l:
                if i < m:
                    m = i
            return m
        @staticmethod
        def maxi(arr):
            return max(arr)
    print('{} {}'.format(Helper.mini(nums), Helper.maxi(nums)))
get_min_max()