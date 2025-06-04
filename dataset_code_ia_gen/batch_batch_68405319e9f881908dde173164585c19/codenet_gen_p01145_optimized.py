import sys

VOWELS = {'a', 'i', 'u', 'e', 'o'}
VOICELESS_CONSONANTS = {'k', 's', 't', 'h', 'p'}
# For identifying consonants, including voiced ones for syllable parsing
CONSONANTS = {'k','s','t','n','h','m','y','r','w','g','z','d','b','p'}

def split_moras(s):
    moras = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        # Sokuon (促音) small tsu
        if c == 'っ':
            # problem states no explicit 'っ' in input but double consonant represent sokuon,
            # so 'っ' won't appear, skip this case
            pass
        # 'n' or "n'"
        if c == 'n':
            if i+1 < n and s[i+1] == "'":
                moras.append("n'")
                i += 2
            else:
                # 'n' mora only if not part of next syllable
                # According to problem, 'n' appears alone only if followed by non-vowel or 'n', 'y'
                # but here we just take single 'n'
                # However parsing order is safe to consider 'n' as mora
                gl = "n"
                i += 1
                moras.append(gl)
        # check for 3-char (C + y + V) mora
        elif i+2 < n and s[i] in CONSONANTS and s[i+1] == 'y' and s[i+2] in {'a','u','o'}:
            moras.append(s[i]+s[i+1]+s[i+2])
            i += 3
        # check for 2-char (C + V) mora
        elif i+1 < n:
            if s[i] in CONSONANTS and s[i+1] in VOWELS:
                moras.append(s[i]+s[i+1])
                i += 2
            # long vowels are represented by repeating vowels a,i,u
            elif s[i] in VOWELS:
                # check if next char is same vowel (long vowel)
                if s[i+1] == s[i]:
                    # long vowel mora is two moras, first usual vowel, second long
                    # but problem represents long vowel by repeated vowels
                    moras.append(s[i])
                    moras.append(s[i+1])
                    i += 2
                else:
                    moras.append(s[i])
                    i += 1
            else:
                # single char vowel or consonant alone
                moras.append(s[i])
                i += 1
        else:
            # last character single
            moras.append(s[i])
            i += 1
    return moras

def parse_moras(s):
    moras = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        # Check n'
        if c == 'n':
            if i+1 < n and s[i+1] == "'":
                moras.append("n'")
                i += 2
                continue
            else:
                # 'n' alone
                moras.append("n")
                i += 1
                continue
        # 3-char mora e.g. ky(a|u|o)
        if i+2 < n and s[i] in CONSONANTS and s[i+1] == 'y' and s[i+2] in {'a','u','o'}:
            moras.append(s[i] + s[i+1] + s[i+2])
            i += 3
            continue
        # 2-char mora consonant + vowel
        if i+1 < n:
            if s[i] in CONSONANTS and s[i+1] in VOWELS:
                moras.append(s[i] + s[i+1])
                i += 2
                continue
            # long vowels check: vowel followed by same vowel (a,i,u)
            if s[i] in VOWELS:
                if s[i] in {'a','i','u'} and s[i+1] == s[i]:
                    # Long vowel represented as two moras
                    moras.append(s[i])
                    moras.append(s[i+1])
                    i += 2
                    continue
                else:
                    moras.append(s[i])
                    i += 1
                    continue
        # single vowel or consonant
        moras.append(c)
        i += 1
    return moras

def is_voiceless_consonant(mora):
    # mora can be 'k', 'ki', 'kyu', etc; voiceless consonants are k,s,t,h,p
    # 'ky' is considered voiceless consonant also
    # So check mora start with one of voiceless consonants:
    # If it's 1 char and in voiceless consonants: 'k','s','t','h','p'
    # If 2 or 3 char mora, first char in voiceless consonants and next is 'y' or vowel
    # Also voiceless consonants + y are voiceless
    if not mora:
        return False
    c = mora[0]
    if c not in VOICELESS_CONSONANTS:
        return False
    # If mora is 1 char consonant with no vowel, unlikely but handle false
    if len(mora) == 1:
        # Single consonant alone
        return False
    # mora starting with voiceless consonant counts
    return True

def get_vowel(mora):
    # vowel in mora is last character if mora length > 1
    # or character itself if single vowel
    # mora can't be empty
    # mora: 'a','ki','kyo','n','n''
    # for 'n' moras, no vowel
    if mora == "n" or mora == "n'":
        return ''
    # look for vowel in mora, from right to left
    for ch in reversed(mora):
        if ch in VOWELS:
            return ch
    return ''

def is_sokuon(mora):
    # sokuon is the small tsu: usually double consonant, represented implicitly
    # no direct 'っ' in input, sokuon represented by doubling consonant
    # but we have moras extracted: no direct indicator
    # problem states '促音（「っ」）' is not appearing alone but represented by doubled consonant in next mora
    # We represent sokuon moras as no moras, only in next mora consonant doubled
    return False # no mora representing sokuon directly

def is_chouon(mora1,mora2):
    # check if mora2 is same vowel long vowel of mora1
    # mora1 and mora2 must both be vowels in {'a','i','u'}
    # long vowels represented by repeated vowels for 'a','i','u' only
    v1 = get_vowel(mora1)
    v2 = get_vowel(mora2)
    if mora1 in VOWELS and mora2 in VOWELS:
        if v1 == v2 and v1 in {'a','i','u'}:
            return True
    return False

def is_sokuon_mora(mora):
    # no direct sokuon moras, represented by double consonant in next mora
    # check if mora length==1 and consonant doubled in next mora for sokuon character
    return False

def check_mora_sokuon(mora):
    # We can't detect sokuon moras directly as per input
    # But we can know 'sokuon' is doubling consonant in next mora
    # So this function is unused.
    return False

def next_after_sokuon(moras, idx):
    # return true if next mora is sokuon
    # input moras do not include sokuon moras as separate moras.
    # Sokuon is represented by doubling consonant in next mora,
    # so sokuon mora doesn't exist alone in moras list.
    # So this function return False always
    return False

def is_consonant(c):
    return c in CONSONANTS

def check_voiceless_with_y(mora):
    # voiceless consonants + 'y' are also voiceless
    # e.g. 'ky' in 'kyo'
    # mora like 'kyo', 'shi' (shi is s consonant but voiced), 'tyu' (tyu is t+yu ?)
    # from problem:
    # "また，これらに「y」が続いたもの（「ky」など）も便宜的に無声子音とみなす．"
    # So mora starting with voiceless consonant and then 'y' count as voiceless consonant
    # check if mora starts with voiceless consonant and second char is 'y'
    if len(mora) >= 2 and mora[0] in VOICELESS_CONSONANTS and mora[1] == 'y':
        return True
    return False

def is_voiceless_mora(mora):
    # Returns True if mora starts with voiceless consonant or voiceless consonant followed by y
    return is_voiceless_consonant(mora) or check_voiceless_with_y(mora)

def expand_moras(s):
    # Handles sokuon by separating it to explicit sokuon mora (represented as 'っ' etc)
    # but problem input does not have 'っ' as input, rather doubled consonants in next mora.
    # We process moras as listed by parse_moras.
    # So no action.
    return parse_moras(s)

def is_sokuon_following(moras, i):
    # sokuon mora is represented as double consonant at start of mora after current mora
    # e.g. in 'kippu' moras would be ['ki','p','pu'] or ['ki','ppu']
    # Our parse_moras represent 'kippu' as ['ki','ppu']
    # So here no separate sokuon mora.
    # But problem states sokuon always written as double consonant in next mora.
    # To check if mora at i+1 is sokuon in 'ki' 'ppu':
    # mora at i+1 has doubled consonant? e.g. two same consonants at start indicated sokuon
    # But no direct doubling in mora representation.
    # We consider that sokuon is represented inside mora like 'ppu'
    if i+1 >= len(moras):
        return False
    m = moras[i+1]
    # check if mora at i+1 begins with doubled consonant
    # mora length >=2, first two chars same consonant
    if len(m) >= 2 and m[0] == m[1] and m[0] in CONSONANTS:
        return True
    return False

def is_next_mora_sokuon(moras, i):
    # same as above, more general
    return is_sokuon_following(moras, i)

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        word = line
        moras = parse_moras(word)

        # precompute is voiceless consonant moras for easier reference
        # also mark vowel of each mora
        vowels = [get_vowel(m) for m in moras]
        voiceless = [is_voiceless_mora(m) for m in moras]

        # we detect long vowels by checking pairs of moras (two vowels repeated)
        # mark which moras are long vowel second part
        long_vowel_idx = set()
        for i in range(len(moras)-1):
            if moras[i] in VOWELS and moras[i+1] in VOWELS:
                if moras[i] == moras[i+1] and moras[i] in {'a','i','u'}:
                    long_vowel_idx.add(i+1)

        n = len(moras)
        # For rule1:
        # vowel i,u short vowels, enclosed in parentheses if:
        # - surrounded by voiceless consonants: mora before and after voiceless consonant
        # - or if following mora is sokuon and at end of word, and previous mora is voiceless consonant
        # Also applies if next mora after vowel is sokuon
        # Also applies if vowel mora followed by sokuon reference in problem

        # For rule2:
        # Regarding vowel 'a' or 'o', if two or more moras in a row start with voiceless consonant + same vowel,
        # all but last vowel in that chain are unvoiced

        # Additionally, no multiple vowels unvoiced consecutively:
        # a vowel is unvoiced only if it is first unvoiced or previous vowel was voiced.

        # We'll store a boolean unvoice flags per mora
        unvoiced = [False]*n

        # Helper: check previous vowel unvoiced or not
        last_unvoiced_idx = -10 # far away

        # Process rule1 for i,u vowels

        # Note: the problem says the vowel is unvoiced if:
        # "母音「i」「u」の短音について，その母音が無声子音にはさまれたとき，"
        # "または無声子音の直後でしかも語句の末尾にあるとき．"
        # Also applies if next mora after vowel is sokuon

        # Let's process rule1 first
        # For each mora with vowel i or u, check condition

        # Need to know if the next mora after this vowel is sokuon or not:
        # sokuon condition: next mora has doubled consonant first two chars same

        # Create a helper function for sokuon check on next mora

        def is_sokuon_after(i):
            # if mora at i+1 exists and starts with doubled consonant
            if i+1 >= n:
                return False
            m = moras[i+1]
            if len(m) >= 2 and m[0] == m[1] and m[0] in CONSONANTS:
                return True
            return False

        for i,mora in enumerate(moras):
            v = vowels[i]
            if v not in {'i','u'}:
                continue
            # morph length check only short vowel (not long)
            # long vowels are repeated vowels, so check next mora to exclude
            if i+1 < n and moras[i+1] == mora:
                # long vowel, skip per problem
                continue
            # check if mora is surrounded by voiceless consonants
            # previous mora voiceless consonant
            prev_voiceless = (i>0 and voiceless[i-1])
            # next mora voiceless consonant or sokuon mora
            next_voiceless = (i+1 < n and voiceless[i+1])
            next_sokuon = is_sokuon_after(i)
            # Also condition: "無声子音の直後でしかも語句の末尾にあるとき"
            # that is mora after is vowel, mora i is vowel, preceding mora is voiceless consonant and mora i is last mora
            # check if previous mora voiceless consonant and mora i is last mora
            # also applies if nexts are sokuon or word end
            at_end = (i == n-1)
            # guaranteed in problem that sokuon never first or last mora
            cond1 = prev_voiceless and next_voiceless
            cond2 = prev_voiceless and at_end
            cond3 = cond1
            cond4 = prev_voiceless and next_sokuon
            if cond1 or cond2 or cond4:
                # unvoice
                # apply unvoicing only if previous vowel was voiced or this is first unvoiced in a row
                if last_unvoiced_idx == -10 or last_unvoiced_idx != i-1:
                    unvoiced[i] = True
                    last_unvoiced_idx = i

        # Process rule2 for vowels a,o
        # "母音「a」「o」について，同一の母音が無声子音とともに連続する2つ以上の拍で現れたとき．ただし，その連続する拍のうちで最後のものについては除外される．"
        # consecutive moras that start with voiceless consonant + vowel a or o and same vowel repeated twice or more
        # long vowels and sokuon excluded, no sokuon or long vowel inside such sequence

        i = 0
        while i < n:
            # skip non a/o vowels or vowels not at start of moras
            v = vowels[i]
            if v not in {'a','o'}:
                i += 1
                continue
            # mora must start with voiceless consonant and vowel a or o
            m = moras[i]
            # mora must NOT be vowel alone to count (vowel alone not starts with consonant)
            # or problem says: "母音「a」「o」について，同一の母音が無声子音とともに連続する2つ以上の拍で現れたとき"
            # so mora should start with voiceless consonant + that vowel
            # so mora has length>=2, first char voiceless consonant, last char vowel
            # must not be sokuon or long vowel moras inside sequence
            if len(m) < 2 or not is_voiceless_mora(m) or v != get_vowel(m):
                i += 1
                continue
            # start of potential chain of same vowel voiceless moras
            start = i
            j = i+1
            while j < n:
                mv = vowels[j]
                mm = moras[j]
                # exclude if sokuon or long vowel or not voiceless consonant + same vowel
                # sokuon or long vowel moras excluded
                # Long vowel moras: repeated vowels (a,i,u)
                if len(mm) < 2 or not is_voiceless_mora(mm) or mv != v:
                    break
                # no sokuon or long vowel inside chain allowed
                # Check if this and previous are adjacent, no sokuon or long vowel in between
                # (checked by mora pattern)
                j += 1
            # length of chain is (j-start)
            length = j - start
            if length >= 2:
                # All but last mora in chain unvoiced
                # Again, apply if no