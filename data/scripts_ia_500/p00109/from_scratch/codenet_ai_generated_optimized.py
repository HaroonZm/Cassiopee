def smart_calculator():
    import sys
    input = sys.stdin.readline
    n = int(input())
    precedence = {'+':1,'-':1,'*':2,'/':2}
    for _ in range(n):
        expr = input().strip()[:-1]  # remove '='
        nums, ops = [], []
        i = 0
        def apply_op():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == '+': nums.append(a+b)
            elif op == '-': nums.append(a-b)
            elif op == '*': nums.append(a*b)
            else: nums.append(int(a/b))
        while i < len(expr):
            c = expr[i]
            if c.isdigit():
                val = 0
                while i < len(expr) and expr[i].isdigit():
                    val = val*10+int(expr[i])
                    i+=1
                nums.append(val)
                continue
            elif c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    apply_op()
                ops.pop()
            else:
                while ops and ops[-1]!='(' and precedence[ops[-1]] >= precedence[c]:
                    apply_op()
                ops.append(c)
            i+=1
        while ops:
            apply_op()
        print(nums[0])