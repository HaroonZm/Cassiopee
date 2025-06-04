while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = 0
        i = 1
        while i <= n // 2:
            m = n - i

            # Test if m is prime (flat version)
            x = m
            prime_m = 1
            if x == 2:
                prime_m = 1
            elif x < 2 or x % 2 == 0:
                prime_m = 0
            else:
                j = 3
                while j <= x ** (1/2):
                    if x % j == 0:
                        prime_m = 0
                        break
                    j += 2

            # Test if i is prime (flat version)
            x = i
            prime_i = 1
            if x == 2:
                prime_i = 1
            elif x < 2 or x % 2 == 0:
                prime_i = 0
            else:
                j = 3
                while j <= x ** (1/2):
                    if x % j == 0:
                        prime_i = 0
                        break
                    j += 2

            if prime_m == 1 and prime_i == 1:
                a += 1
            i += 1
        print(a)