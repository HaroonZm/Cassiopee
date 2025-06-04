# Cette solution lit la requête et l'objet YAML, puis :
# 1. Parse le YAML selon l'indentation pour reconstituer un dictionnaire imbriqué.
# 2. Parcourt la structure selon la requête.
# 3. Affiche le résultat selon les consignes.

import sys

sys.setrecursionlimit(10**7)

def main():
    # Lecture de la requête (ex: .tweets.1)
    query_line = sys.stdin.readline().rstrip('\n')
    # Extraire les clés depuis la requête en splittant par '.'
    # Le premier caractère est '.', donc on ignore la première partie vide.
    query_keys = query_line.split('.')[1:]
    
    # Lecture du reste du stdin qui correspond au YAML
    yaml_lines = [line.rstrip('\n') for line in sys.stdin]
    
    # On parse le YAML en dictionnaire imbriqué
    # Le parsing se fait par la gestion de l'indentation
    # Retourne un tuple (mapping, index de la prochaine ligne non consommée)
    def parse_mapping(start_line_index, current_indent):
        mapping = {}
        i = start_line_index
        while i < len(yaml_lines):
            line = yaml_lines[i]
            # Compter l'indentation (nombre d'espaces au début)
            indent = 0
            while indent < len(line) and line[indent] == ' ':
                indent += 1
            
            if indent < current_indent:
                # Fin de ce mapping car moins indenté que ce niveau
                break
            
            if indent > current_indent:
                # Ligne indentée plus que attendu => erreur de structure ou appartient 
                # à un sous-mapping déjà traité (should not happen si bien formé)
                # Ne pas traiter ici, revient dans appel récursif
                break
            
            # Maintenant indent == current_indent
            # On traite la ligne
            # Exemple : key: value ou key:\n
            
            content = line[indent:]
            # Trouver la position du premier ':' pour séparer key et value
            colon_pos = content.find(':')
            key = content[:colon_pos]
            rest = content[colon_pos+1:]
            
            # Rest peut être ' value' ou '\n' vide (enfin ligne sans suite) signifiant sous-mapping
            if rest == '':
                # c'est une ligne avec clé suivie d'un mapping imbriqué au niveau indent+1
                # Parse récursivement le mapping imbriqué
                sub_mapping, next_line = parse_mapping(i+1, current_indent+1)
                mapping[key] = sub_mapping
                i = next_line
            else:
                # Ligne avec valeur string
                # rest commence par ' ' puis la valeur, selon format : ' value'
                # Enlever l'espace initial avant la valeur
                if rest.startswith(' '):
                    value = rest[1:]
                else:
                    value = rest
                mapping[key] = value
                i += 1
        return mapping, i
    
    # Parser tout à partir de la ligne 0 avec indent 0
    root_mapping, _ = parse_mapping(0, 0)
    
    # Parcourir la structure avec les clés du query
    cur = root_mapping
    for k in query_keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            # propriété non trouvée
            print("no such property")
            return
    
    # Maintenant cur est la valeur finale demandée
    # Si objet (dict) => "object"
    # Si string => 'string "<valeur>"'
    if isinstance(cur, dict):
        print("object")
    else:
        # valeur string
        print(f'string "{cur}"')

if __name__ == "__main__":
    main()