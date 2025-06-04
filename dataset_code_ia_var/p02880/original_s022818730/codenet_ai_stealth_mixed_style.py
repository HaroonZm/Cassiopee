n = int(input())

def is_valid(number):
    # style procédural avec retour de valeur
    for i in range(1, 10):
        if number % i == 0:
            if number // i <= 9 and number / i == number // i:
                return True
    return False

result = None
class Checker:
    # style orienté objet inutilement
    def __init__(self, val):
        self.val = val
    def check(self):
        global result
        result = is_valid(self.val)

(lambda x: Checker(x).check())(n) # style fonctionnel avec lambda

if result:
    print("Yes")
else:
    import sys
    sys.stdout.write("No\n")