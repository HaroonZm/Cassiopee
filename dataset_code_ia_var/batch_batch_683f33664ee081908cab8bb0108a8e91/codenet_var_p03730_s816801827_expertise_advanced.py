A, B, C = map(int, input().split())
residues = {(i * A) % B for i in range(B)}
print('YES' if C in residues else 'NO')