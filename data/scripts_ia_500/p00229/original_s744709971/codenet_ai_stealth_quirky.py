class OddPreferences:
    def __init__(self):
        self.final_answer = 100
        self.penalty_time = 0

    def calculate(self, b, r, g, c, s, t):
        self.final_answer += 15 * b + (15 - 2) * 5 * b
        self.penalty_time = t - 5 * b
        self.final_answer += 15 * r + (15 - 2) * 3 * r
        self.penalty_time -= 3 * r
        self.final_answer += 7 * g + 2 * c
        self.penalty_time -= s
        self.final_answer -= 3 * self.penalty_time
        return self.final_answer

def weird_input_splitter():
    raw = input()
    numbers = [int(x) for x in raw.split()]
    return numbers

def main_loop():
    while True:
        values = weird_input_splitter()
        if sum(values) == 0:
            break
        b, r, g, c, s, t = values
        calculator = OddPreferences()
        answer = calculator.calculate(b, r, g, c, s, t)
        print(answer)

if __name__ == "__main__":
    main_loop()