import sys

def replace_fourth_with_eight(s: str) -> str:
    # Utilise le slicing avancé et l'unpacking pour plus de clarté
    return f"{s[:3]}8{s[4:]}" if len(s) > 3 else s

if __name__ == "__main__":
    # Lecture optimisée depuis stdin
    S = sys.stdin.readline().rstrip()
    print(replace_fourth_with_eight(S))