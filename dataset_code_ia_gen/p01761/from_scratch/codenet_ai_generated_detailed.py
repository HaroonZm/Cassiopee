# Programme complet pour le problème "B : Books / 本"
# Solution en Python avec commentaires détaillés expliquant l'approche

import sys

def date_to_int(date_str):
    """
    Convertit une date au format 'YYYY/MM/DD' en un entier YYYYMMDD
    pour faciliter la comparaison.
    Ex : '2014/07/07' -> 20140707
    """
    y, m, d = date_str.split('/')
    return int(y)*10000 + int(m)*100 + int(d)

def matches(query_value, book_value):
    """
    Vérifie si book_value 'contient' query_value, ou si query_value est '*'.
    La correspondance est sensible à la casse.
    """
    if query_value == '*':
        return True
    return query_value in book_value

def main():
    input = sys.stdin.readline

    N = int(input())
    books = []
    for _ in range(N):
        # Lire chaque livre : title, author, date
        line = input().strip()
        # Le format est "title author date" sur une seule ligne
        # selon l'exemple, mais dans l'énoncé c'est 3 lignes par livre ?
        # → Reprendre l'énoncé : "続くN行にはそれぞれの本に関する情報が続く"
        # Le sample input montre qu'une ligne contient title author date
        # Donc on parse tout sur une ligne :
        parts = line.split()
        title = parts[0]
        author = parts[1]
        date = parts[2]
        books.append({
            'title': title,
            'author': author,
            'date_str': date,
            'date_int': date_to_int(date)
        })

    Q = int(input())
    queries = []
    for _ in range(Q):
        q_line = input().strip()
        # Selon l'énoncé, chaque requête comporte 4 mots sur 1 ligne
        # : Q_title, Q_author, Q_date_from, Q_date_to
        q_title, q_author, q_date_from, q_date_to = q_line.split()
        queries.append({
            'title': q_title,
            'author': q_author,
            'date_from_str': q_date_from,
            'date_to_str': q_date_to,
            'date_from_int': date_to_int(q_date_from) if q_date_from != '*' else None,
            'date_to_int': date_to_int(q_date_to) if q_date_to != '*' else None,
        })

    # Pour chaque requête, filtrer les livres qui correspondent sur les 4 critères
    for idx, q in enumerate(queries):
        results = []
        for book in books:
            # tester titre
            if not matches(q['title'], book['title']):
                continue
            # tester auteur
            if not matches(q['author'], book['author']):
                continue
            # tester date_from
            if q['date_from_int'] is not None and book['date_int'] < q['date_from_int']:
                continue
            # tester date_to
            if q['date_to_int'] is not None and book['date_int'] > q['date_to_int']:
                continue
            # si tous les tests sont passés, ajout au résultat
            results.append(book['title'])

        # sortie : titres un par un, dans l'ordre d'entrée
        for title in results:
            print(title)

        # Entre chaque requête, mettre une ligne vide sauf après la dernière
        if idx != Q-1:
            print()

if __name__ == '__main__':
    main()