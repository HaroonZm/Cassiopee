class GrowthCommand:
    def __init__(self, plant):
        self.plant = plant

    def execute(self):
        raise NotImplementedError("Subclasses should implement this!")

class NobiroCommand(GrowthCommand):
    def execute(self):
        self.plant.grow(self.plant.a)

class TidimeCommand(GrowthCommand):
    def execute(self):
        self.plant.grow(self.plant.b)

class KareroCommand(GrowthCommand):
    def execute(self):
        self.plant.reset()

class Plant:
    def __init__(self, initial_length, a, b):
        self.length = initial_length
        self.a = a
        self.b = b

    def grow(self, delta):
        new_length = self.length + delta
        self.length = max(new_length, 0)

    def reset(self):
        self.length = 0

class CommandFactory:
    def __init__(self, plant):
        self.plant = plant
        self._commands_map = {
            "nobiro": NobiroCommand,
            "tidime": TidimeCommand,
            "karero": KareroCommand
        }

    def create_command(self, command_str):
        command_class = self._commands_map.get(command_str)
        if not command_class:
            raise ValueError(f"Unknown command: {command_str}")
        return command_class(self.plant)

class PlantSimulator:
    def __init__(self, initial_length, a, b, commands):
        self.plant = Plant(initial_length, a, b)
        self.factory = CommandFactory(self.plant)
        self.commands_str = commands

    def simulate(self):
        for cmd_str in self.commands_str:
            command = self.factory.create_command(cmd_str)
            command.execute()
        return self.plant.length

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    x, a, b = map(int, input_data[0].split())
    n = int(input_data[1])
    commands = input_data[2:2+n]

    simulator = PlantSimulator(x, a, b, commands)
    result = simulator.simulate()
    print(result)

if __name__ == "__main__":
    main()