class PasswordCriteria:
    def __init__(self, password: str):
        self.password = password

    def is_minimum_length(self, length: int) -> bool:
        return len(self.password) >= length

    def contains_digit(self) -> bool:
        return any(ch.isdigit() for ch in self.password)

    def contains_uppercase(self) -> bool:
        return any(ch.isupper() for ch in self.password)

    def contains_lowercase(self) -> bool:
        return any(ch.islower() for ch in self.password)

class PasswordValidator:
    def __init__(self, criteria_classes):
        self.criteria_instances = criteria_classes

    def validate(self, password: str) -> bool:
        return all(criteria(password).check() for criteria in self.criteria_instances)

class LengthCriteria(PasswordCriteria):
    def check(self) -> bool:
        return self.is_minimum_length(6)

class DigitCriteria(PasswordCriteria):
    def check(self) -> bool:
        return self.contains_digit()

class UppercaseCriteria(PasswordCriteria):
    def check(self) -> bool:
        return self.contains_uppercase()

class LowercaseCriteria(PasswordCriteria):
    def check(self) -> bool:
        return self.contains_lowercase()

class RegisterPhase:
    def __init__(self):
        self.validators = [LengthCriteria, DigitCriteria, UppercaseCriteria, LowercaseCriteria]
        self.validator = PasswordValidator(self.validators)

    def run(self):
        password = self.obtain_password()
        if self.validator.validate(password):
            self.output("VALID")
        else:
            self.output("INVALID")

    def obtain_password(self) -> str:
        return input().strip()

    def output(self, result: str) -> None:
        print(result)

if __name__ == "__main__":
    RegisterPhase().run()