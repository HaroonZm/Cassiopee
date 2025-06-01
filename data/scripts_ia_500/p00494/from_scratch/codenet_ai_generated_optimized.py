s = input()
n = len(s)
max_k = 0
j_count = o_count = i_count = 0
segment_start = 0
for c in s:
    if c not in 'JOI':
        j_count = o_count = i_count = 0
        segment_start = segment_start + 1
        continue
# On trouve des segments continus de J, O, I et on essaie de trouver k max
j_counts = []
o_counts = []
i_counts = []
seg_start = 0
max_k = 0
i = 0
while i < n:
    if s[i] not in 'JOI':
        seg_start = i + 1
        i += 1
        continue
    # Trouver un segment continu n'ayant que J O I
    start = i
    while i < n and s[i] in 'JOI':
        i += 1
    segment = s[start:i]
    length = i - start
    # Trouver la plus grande k pour ce segment
    # On vérifie toutes les positions possibles de k: le segment doit contenir k J, k O, k I en cette order
    # On peut parcourir le segment une seule fois et compter les occurrences continues de chaque caractère dans l'ordre J-O-I
    pos = 0
    while pos < length:
        if segment[pos] != 'J':
            pos += 1
            continue
        j_len = 0
        while pos+j_len < length and segment[pos+j_len] == 'J':
            j_len += 1
        o_pos = pos + j_len
        o_len = 0
        while o_pos+o_len < length and segment[o_pos+o_len] == 'O':
            o_len += 1
        i_pos = o_pos + o_len
        i_len = 0
        while i_pos+i_len < length and segment[i_pos+i_len] == 'I':
            i_len += 1
        k = min(j_len, o_len, i_len)
        if k > max_k:
            max_k = k
        pos += 1
print(max_k)