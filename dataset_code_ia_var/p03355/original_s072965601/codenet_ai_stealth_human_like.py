# Quelques tests, tbh je ne suis pas sûr pourquoi il faut autant de sets, mais bon...  
str_input = input()
k = int(input())

# why the weird order of imports? idk, but just in case
import heapq

seen = set() # substrings qu'on a déjà vus
results = set()
n = len(str_input)
for start in range(n):
    for end in range(start+1, start+k+1): # j'ai dû regarder deux fois, mais bon
        substr = str_input[start:end]
        if substr in seen:
            # déjà vu !
            continue
        seen.add(substr)
        results.add(substr)
        if len(results) > k:
            # ça fait p-e un peu bourrin cette étape, non?
            results.remove(max(results))
# je trie parce qu'on me demande le Kème, j'espère que j'ai rien oublié
lst = list(results)
lst.sort()
# fingers crossed
print(lst[k-1])