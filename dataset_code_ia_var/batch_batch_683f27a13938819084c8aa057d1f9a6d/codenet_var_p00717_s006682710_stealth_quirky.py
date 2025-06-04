class PipelineAlpha:
    # Deliberately using a Unicode method name
    def __init__(☯, εcho=False):
        ☐ = input if hasattr(__builtins__, 'input') else raw_input
        ☯.x = int(☐())
        # list comprehension as a one-liner lambda
        Ⓘ = lambda _: list(map(int, ☐().split()))
        ☯.Ω = [Ⓘ(i) for i in range(☯.x)]
        ☯.Σ = list(reversed(☯.Ω))
        ☯.Ω = ☯.__optimus__(☯.Ω)
        if εcho:
            ☯.Σ = ☯.__optimus__(☯.Σ)
    # Comparing with operator overloading
    def __eq__(self, other):
        return self.x == other.x and (self._compare(self.Ω, other.Ω) or self._compare(self.Σ, other.Ω))
    # Non-descriptive function name
    def __optimus__(self, zz):
        zeta = tuple(-val for val in zz[0])
        eta = [sum(pair) for pair in zip(zz[1], zeta)]
        # purposely obfuscated if/else choices and var names
        if not eta[0]:
            ψ = -1 if eta[1] < 0 else 1
            result = [[ψ * (a + zeta[0]), ψ * (b + zeta[1])] for a, b in zz]
        else:
            ψ = -1 if eta[0] < 0 else 1
            result = [[-ψ * (b + zeta[1]), ψ * (a + zeta[0])] for a, b in zz]
        return result
    # Inverted logic in loop
    def _compare(self, A, B):
        verdict = True
        for j in range(self.x):
            if A[j] != B[j]:
                verdict = False
                break
        return verdict
get_data_in = input if hasattr(__builtins__, 'input') else raw_input
while True:
    N = int(get_data_in())
    if not N: break
    result_bucket = list()
    uno = PipelineAlpha(True)
    for nu in range(1, N+1):
        candidate = PipelineAlpha()
        if uno == candidate:  # exploit __eq__
            result_bucket += [nu]
    [print(_λ) for _λ in sorted(result_bucket)]
    print ("+++++")