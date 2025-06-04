class Panel:
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    ORDER = [LEFT, UP, DOWN, RIGHT]  # For orientation and potential future rules

class Foot(str):
    LEFT = 'L'
    RIGHT = 'R'
    @staticmethod
    def opposite(foot):
        return Foot.RIGHT if foot == Foot.LEFT else Foot.LEFT

class Orientation:
    # Facing forward means left foot always on left panels (L or U), right foot on right panels (R or D)
    # legs never cross if left foot panel <= right foot panel in defined order (L < U < D < R?)
    # We define an order that reflects horizontal position:
    # let's map panels to x coordinates: L = -1, U = 0, D=0, R=1
    _pos = {Panel.LEFT: -1, Panel.UP: 0, Panel.DOWN: 0, Panel.RIGHT: 1}
    @staticmethod
    def is_valid(left_panel, right_panel):
        # Conditions:
        # left foot on left side panels: L or U
        # right foot on right side panels: R or D
        left_ok = left_panel in {Panel.LEFT, Panel.UP}
        right_ok = right_panel in {Panel.RIGHT, Panel.DOWN}
        if not (left_ok and right_ok):
            return False
        # Legs never cross means left foot position <= right foot position
        # based on _pos values:
        return Orientation._pos[left_panel] <= Orientation._pos[right_panel]

class StepSequenceValidator:
    def __init__(self, score):
        self.score = score

    def is_natural(self):
        # We must find a foot assignment alternating left/right starting with left foot on first arrow,
        # no two consecutive steps on the same panel,
        # and maintaining orientation rules at every step (legs don't cross and facing forward).
        #
        # We try to assign each arrow to a foot:
        # steps alternate: indexes even => left foot, odd => right foot
        # for each arrow, assign that step to the appropriate foot,
        # and keep track of previous panels for both feet to ensure no consecutive same panel,
        # then check orientation.
        #
        # Because the feet stand on panels, we store last panel for left and right foot,
        # and at each step, new step must not be on same panel as previous step of the same foot.
        #
        # But orientation depends on positions of the feet after each step:
        # left panel and right panel
        #
        # If at any point conditions fail, return False
        #
        # To consider all possible start configurations for first step?
        # The problem statement implicitly assumes first step is on left foot (left foot steps and right foot steps appear in turn)
        # So index 0 is left foot, index 1 right foot, etc.
        #
        # We try to determine a sequence that fulfills the constraints by assigning panels carefully.
        # However, since the input is a sequence of panels and the foot assignment is fixed by position (step i by foot: i%2 == 0 left, else right),
        # the only choice is to see if possible according to constraints.
        #
        # The same panel cannot be stepped on two consecutive arrows (same foot).
        # The player must maintain orientation so legs never cross and body faces forward.
        #
        # Given that foot assignment is fixed by step parity, we just check if sequence fulfills constraints.

        left_panel = None
        right_panel = None
        last_panel_left = None
        last_panel_right = None
        n = len(self.score)

        for i, panel in enumerate(self.score):
            foot = Foot.LEFT if i % 2 == 0 else Foot.RIGHT

            # Check if same foot steps on same panel consecutively
            if foot == Foot.LEFT:
                if last_panel_left == panel:
                    return False
                last_panel_left = panel
            else:
                if last_panel_right == panel:
                    return False
                last_panel_right = panel

            # After updating last_panel, we check orientation based on current panels
            # For orientation, we need to know where both feet currently stand.
            # If one foot hasn't stepped yet (e.g. at step 0 only left foot stepped), we can consider right foot still on none (no violation)
            current_left = last_panel_left
            current_right = last_panel_right
            if current_left is not None and current_right is not None:
                if not Orientation.is_valid(current_left, current_right):
                    return False
        
        return True

class InputParser:
    def __init__(self, raw_input):
        self.raw_input = raw_input

    def parse(self):
        lines = self.raw_input.strip().split('\n')
        count = int(lines[0])
        scores = lines[1:]
        assert count == len(scores)
        return scores

class DDRNaturalChecker:
    def __init__(self, inputs):
        self.inputs = inputs

    def process(self):
        results = []
        for score in self.inputs:
            validator = StepSequenceValidator(score)
            results.append("Yes" if validator.is_natural() else "No")
        return results

def main():
    import sys
    input_data = sys.stdin.read()
    parser = InputParser(input_data)
    scores = parser.parse()
    checker = DDRNaturalChecker(scores)
    results = checker.process()
    print('\n'.join(results))

if __name__ == "__main__":
    main()