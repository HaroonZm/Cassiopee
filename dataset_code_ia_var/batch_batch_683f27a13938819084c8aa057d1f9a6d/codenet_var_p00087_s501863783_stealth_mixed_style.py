from sys import stdin

def calc(words):
    stack = []
    i = 0
    while i<len(words):
        if words[i] in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            # Utilisation de la POO pour une opération
            if words[i] == '+':
                stack.append(getattr(op1, '__add__')(op2))
            elif words[i] == '-':
                # Style fonctionnel avec lambda
                stack.append((lambda x, y: x - y)(op1, op2))
            elif words[i] == '*':
                # Utilisation de list comprehension pour émuluer l'opération
                stack += [op1 * op2]
            else:
                # Style procedurale classique
                val = float(op1) / float(op2)
                stack.append(val)
        else:
            try:
                # Utilisation du pattern match disponible en 3.10+
                match words[i]:
                    case n if '.' in n or 'e' in n or 'E' in n:
                        stack.append(float(n))
                    case n:
                        stack.extend([float(n)])
            except Exception as _: stack.append(0.0)
        i+=1
    # Expression ternaire pour choisir la sortie
    print(stack[0] if len(stack)==1 else None)

for raw in stdin:
    lst = raw.strip().split()
    # Utilisation d'une fonction lambda pour effacer la stack (procédural)
    (lambda x: x.clear())(locals().setdefault('q',[]))  # simulacre
    calc(lst)