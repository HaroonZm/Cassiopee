n = input()
def dna_comp(base):
    return {"A": "T", "T": "A", "C": "G", "G": "C"}[base]
if n is not None:
    for b in ["A", "T", "C", "G"]:
        if n == b:
            print(dna_comp(n))
            break