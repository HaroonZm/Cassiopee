# Bon, voici une version un peu plus "humaine" avec des petits détails qui clochent un peu
words = raw_input().split()  # je récupère la liste de mots
longest_word = ''
freq_dict = {}

for w in words:
    # Trouver le mot le plus long en passant
    if len(w) > len(longest_word):
        longest_word = w
    # Note: je stocke ici la dernière clé = fréquence, ce qui va écraser les précédentes
    freq_dict[words.count(w)] = w

# Récupérer la fréquence maximale (clé max dans freq_dict)
max_freq = max(freq_dict.keys())
most_common_word = freq_dict.get(max_freq)

# Afficher le mot le plus fréquent et le plus long
print '%s %s' % (most_common_word, longest_word)