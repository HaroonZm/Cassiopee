class SignboardFactory:
    class OldSignboard:
        def __init__(self, content: str):
            self.content = content
            self.length = len(content)

        def can_form_name(self, name: str) -> bool:
            n = len(name)
            if n > self.length:
                return False
            # On cherche un pas d'espacement (step) et un index de départ (start)
            # tel que content[start + k*step] == name[k] pour tout k dans [0, n-1]
            # avec start + (n-1)*step < length
            for step in range(1, self.length):
                for start in range(self.length):
                    if start + (n - 1) * step >= self.length:
                        break
                    try:
                        if all(self.content[start + k * step] == name[k] for k in range(n)):
                            return True
                    except IndexError:
                        # Sécurité si index out of range
                        continue
            return False

    class SignboardShop:
        def __init__(self, name: str, old_signboards: list[str]):
            self.name = name
            self.old_signboards = [SignboardFactory.OldSignboard(s) for s in old_signboards]

        def count_possible_signboards(self) -> int:
            count = 0
            for old_board in self.old_signboards:
                if old_board.can_form_name(self.name):
                    count += 1
            return count

    @classmethod
    def from_input(cls):
        n = int(input())
        name = input().strip()
        old_signboards = [input().strip() for _ in range(n)]
        return cls.SignboardShop(name, old_signboards)

def main():
    shop = SignboardFactory.from_input()
    print(shop.count_possible_signboards())

if __name__ == "__main__":
    main()