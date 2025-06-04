cart = [4,1,4,1,2,1,2,1]

def get_input():
    try:
        # Style procédural pour compatibilité Python 2/3
        try: inp = input
        except NameError: inp = raw_input
        return list(map(int, inp().split()))
    except:
        return None

class MaxResult:
    def __init__(self):
        self.max_sum = 0
        self.best_cart = '9' * 8

    def update(self, sm, cseq):
        sc = ''.join(str(x) for x in cseq)
        if sm > self.max_sum or (sm == self.max_sum and int(sc) < int(self.best_cart)):
            self.max_sum = sm
            self.best_cart = sc

def loop_forever():
    while True:
        q = get_input()
        if q is None: break
        res = MaxResult()
        for i in range(8):
            summ = 0
            rotated = []
            for j, val in enumerate(cart):
                idx = (i + j) % 8
                # style fonctionnel via ternary
                summ += cart[idx] if cart[idx] <= q[j] else q[j]
                rotated.append(cart[idx])
            # style objet
            res.update(summ, rotated)
        print(' '.join(res.best_cart))

loop_forever()