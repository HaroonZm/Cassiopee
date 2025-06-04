import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

def build_failure(pattern):
    m = len(pattern)
    fail = [0]*m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j
    return fail

def kmp_next_table(s, patterns):
    # Pour chaque pattern, on calcule la transition f[i][c]
    # ici, s est une chaîne, on veut a chaque indice le passage dans l'automate
    # On travaille avec la même technique pour chaque saison word
    next_tables = []
    # On retourne un tableau: pour chaque saison word k 
    #   un tableau next: pour chaque etat (0..len) et caractère 'a'..'z' next state
    for pat in patterns:
        m = len(pat)
        fail = build_failure(pat)
        nxt = [dict() for _ in range(m+1)]
        for i in range(m+1):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if i < m and c == pat[i]:
                    nxt[i][c] = i+1
                else:
                    if i == 0:
                        nxt[i][c] = 0
                    else:
                        nxt[i][c] = nxt[fail[i-1]][c]
        next_tables.append(nxt)
    return next_tables

def main():
    input=sys.stdin.readline
    while True:
        N,M,K=map(int,input().split())
        if N==0 and M==0 and K==0:
            break
        connections = [input().split() for _ in range(N)]
        seasonwords = [input().strip() for _ in range(K)]

        # construire dictionnaire adjacence: from word index -> list of to word indices
        # on doit travailler avec index des mots
        # d'abord recuperer tous les mots apparaissant dans connections
        words_set = set()
        for f,t in connections:
            words_set.add(f)
            words_set.add(t)
        words = list(words_set)
        words_id = {w:i for i,w in enumerate(words)}
        # creer adjacency list
        adj = [[] for _ in range(len(words))]
        for f,t in connections:
            adj[words_id[f]].append(words_id[t])

        # important: on generera une phrase de M mots
        # dp[pos][word][season_mask][season_word_len][season_word_idx] = nombre de façons d'avoir construit
        # pos mots, le dernier mot est word, les saison words vus par des masques, 
        # on va factoriser autrement le matching du saison word dans la concaténation: 
        # on doit reconnaitre un seul saison word unique apparu une seule fois dans la concaténation des mots
        # Le matching se fait via les transitions des automates des saison words.
        # On construit un automate multi-mot

        # On fait une seule automatisation combinée des saison words:
        # On va garder un état pour chacun des saison words: position de matching dans la saison word
        # C'est un vecteur de K int (0..len seasonword)
        # Mais ca explose (len max 20, K max 30) => 21^30 trop gros

        # alternative: Puisqu'on doit avoir un seul saison word apparaissant une fois, 
        # on peut aussi stocker plutôt l'état suivant pour chaque saisonword:
        # Mais meme idee ca explose

        # On a la condition que qu'un seul saison word doit apparaître une fois dans la phrase.
        # On note que la saison word peut être traversée sur la frontière entre mots, c'est la concat des mots

        # On va donc modéliser par un automates combiné des saisonwords "acceptants":
        # On crée pour chaque saison word son automate de kmp (en `next_tables` ),
        # et on stocke pour l'etat de dp:
        # - pos actuel (indice mot)
        # - word actuel (dernier mot choisi)
        # - quelle saison word a été détectée (0: aucune, 1..K: et laquelle)
        # - pour la saison word détectée : un booléen "vu une fois" (quand on a fini de la matcher)
        # - mais on a aussi les états de matching partiel pour chaque saison word
        # 
        # idée: A cause de la condition d'une fois 1 seul saison word et une seule fois,
        # on ne peut pas matcher de 2 saisons differentes,
        # donc on mémorise quelle saison word c'est (0 = aucune, s en 1..K),
        # si aucune, on peut matcher les saison words,
        # si on a choisi une saison word, on ne veut plus matcher les autre et vérifier que c'est une seule apparition.

        # pour ne pas explose, on combine les états des automates KMP dans un tuple (états pour chaque saison word)
        # on limitera K à 30 et longueurs max 20 c'est plus ou moins possible
        # mais 21^30 out of question.

        # on suivant la recommandation: "季語は単語の接続の境界をまたいで出現してもよい"
        # donc c'est bien la concat des mot

        # on représente les mots par leur chaine, car pour chaque étape la suite des mots crée une phrase
        # on doit faire le dp sur pos et mot actuel et les etats des K automates

        # Solution alternative : construire un automatisme Aho-Corasick pour toutes les saison words en même temps,
        # cela gère tous les motifs dans une structure plus compacte.

        # On encode les mots par leur indices.
        # On construit l'automate d'Aho-Corasick des saison words.

        # On fera DP sur:
        # position (0..M)
        # mot actuel (id)
        # état du automate Aho-Corasick (nombre d'états <= somme(lengths des saison words))

        # dans cet état, on sait quelles saisons sont trouvées.

        # On doit vérifier qu'exactement un saison word apparait une fois (et pas plus)
        # L'automate d'Aho-Corasick donne l'état courant et les saisons détectées à cette position
        # car on peut tomber sur un mot de saison word qui apparait, on note cela

        # On renforcera pour stocker le nombre d'apparition des saison word: mais cela peut être multiple
        # On note la contrainte: une seule saison word apparaissant une fois.

        # Donc on fait états en mémorisant:
        # - automate state (0..ac_size-1)
        # - quel saison word a été rencontré? (0 = aucun, s=1..K)
        # - si on a rencontré un saison word, alors on doit éviter d'en rencontrer un autre différent (<=1)
        # Si on rencontre 2 fois la même saison word (2 occurrences) => rejet

        # Donc on stockera dans le dp
        # dp[pos][word][ac_state][season_found]
        # season_found = 0 => aucun
        # season_found = s (1..K) => saison s vu une fois
        # season_found = -1 => plus d'une occurence ou >1 saison word differentes (non valide)

        # dans dp on ne poursuivra pas les états où season_found=-1

        # Avant de coder, construire AC

        # Construct Aho Corasick
        class ACAutomaton:
            def __init__(self):
                self.next = [{}]
                self.fail = [0]
                self.output = [set()]
            def add_word(self, w, idx):
                cur = 0
                for c in w:
                    if c not in self.next[cur]:
                        self.next[cur][c] = len(self.next)
                        self.next.append({})
                        self.fail.append(0)
                        self.output.append(set())
                    cur = self.next[cur][c]
                self.output[cur].add(idx)
            def build(self):
                from collections import deque
                q = deque()
                for c,v in self.next[0].items():
                    q.append(v)
                while q:
                    r = q.popleft()
                    for c,nxt in self.next[r].items():
                        self.fail[nxt] = self.next[self.fail[r]].get(c, 0)
                        self.output[nxt] |= self.output[self.fail[nxt]]
                        q.append(nxt)
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c not in self.next[r]:
                            self.next[r][c] = self.next[self.fail[r]].get(c,0)
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c not in self.next[0]:
                        self.next[0][c] = 0

        ac = ACAutomaton()
        for i, w in enumerate(seasonwords):
            ac.add_word(w, i+1) # saison word index from 1
        ac.build()

        word_strings = words
        nwords = len(words)
        ac_states = len(ac.next)

        # On precompute pour chaque mot et état ac_state, l'etat ac apres lecture de ce mot
        # et aussi la liste des saison words rencontrées (set)

        # On precompute la transition ac sur un mot entier:
        # pour chaque état ac_state:
        # on marche caractere par caractere du mot
        # au final on aura:
        #   next_state, set_saison_words found

        # dp dimensions:
        # pos : 0..M
        # cur_word: 0..nwords-1
        # ac_state: 0..ac_states-1
        # season_found: 0..K pour le numéro de saison word trouvé, ou 0 pour aucun

        # Pourato: stocker dp[pos][cur_word][ac_state][season_found] = nombre de façon

        # Compression mémoire:
        # On va faire dp en "pos" itératif, on garde un dict/map ou array pour dp
        # On gardera dp_current et dp_next

        import collections

        trans = [[0]*ac_states for _ in range(nwords)]
        secr = [set() for _ in range(nwords)]

        for wi in range(nwords):
            w = word_strings[wi]
            for st in range(ac_states):
                cur = st
                found = set()
                for c in w:
                    cur = ac.next[cur][c]
                    found |= ac.output[cur]
                trans[wi][st] = cur
                secr[wi] = secr[wi].union(found) if secr[wi] else found

        # maintenant dp
        # init: pos=1, dp[pos][word][ac_state][0] = 1 pour toutes word, ac_state=0 (etat initial AC)

        # mais saisonfound=0 = aucun
        # (pour saisonfound=0..K, 0=c=aucun, else un seul saisonword trouvé)

        # attention quand on combine found lors du passage d'un mot:
        # si saisonfound=0 et found dans mot = {s}, nouveau seasonfound = s si len(found)==1

        # si found multiple saisonword en un mot c'est invalid direct (car 2 saisonword different a 1 occurrence dans le meme mot), dp = 0 pour ce chemin

        # si seasonfound=s (avec s>0) et found={s'}, alors si s' == s, il s'agit d'un deuxième apparition => invalid -> poubelle

        # si s' != s : on a un deuxième saisonword différent ou on a déjà rencontré un saisonword et on en retrouve un autre -> invalid

        # si found vide => seasonfound ne change pas

        # si found multiple elements => invalid

        dp_cur = [[[0]*(K+1) for _ in range(ac_states)] for _ in range(nwords)]
        for w in range(nwords):
            dp_cur[w][0][0] = 1

        for _ in range(1,M):
            dp_next = [[[0]*(K+1) for _ in range(ac_states)] for _ in range(nwords)]
            for w in range(nwords):
                for acs in range(ac_states):
                    for sez in range(K+1):
                        val = dp_cur[w][acs][sez]
                        if val == 0:
                            continue
                        for nw in adj[w]:
                            nxt_acs = trans[nw][acs]
                            found = ac.output[nxt_acs]
                            # checked multiples
                            if len(found) > 1:
                                continue
                            if len(found) == 1:
                                f = next(iter(found))
                                if sez == 0:
                                    sez2 = f
                                else:
                                    if sez == f:
                                        # deuxième apparition du même saisonword
                                        continue
                                    else:
                                        # deuxième saisonword different
                                        continue
                            else:
                                sez2 = sez
                            dp_next[nw][nxt_acs][sez2] = (dp_next[nw][nxt_acs][sez2] + val) % MOD
            dp_cur = dp_next

        # somme sur pos=M, mot, ac_state, saisonfound qui est !=0 (exactement 1 saisonword apparent)
        ans = 0
        for w in range(nwords):
            for acs in range(ac_states):
                for sez in range(1,K+1):
                    ans = (ans + dp_cur[w][acs][sez])%MOD
        print(ans)

if __name__ == "__main__":
    main()