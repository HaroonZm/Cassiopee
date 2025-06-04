def get_input_numbers():
    return list(map(int, input().split()))

def get_input_commands():
    return input()

def make_dice(men_values):
    return Dice(*men_values)

def process_commands(dice_instance, commands):
    for c in commands:
        process_single_command(dice_instance, c)

def process_single_command(dice_instance, command):
    dice_instance.move_dice(command)

def print_top_number(dice_instance):
    print(dice_instance.show_num())

def main():
    men_values = get_input_numbers()
    commands = get_input_commands()
    d = make_dice(men_values)
    process_commands(d, commands)
    print_top_number(d)

class Dice:
    def __init__(self, men1, men2, men3, men4, men5, men6):
        self.men = self._create_men_list(men1, men2, men3, men4, men5, men6)
        self.current_men = self._init_current_men()
        self.men_udlr = self._init_men_udlr()
        self.move_d = self._init_move_d()
        
    def _create_men_list(self, men1, men2, men3, men4, men5, men6):
        return [men1, men2, men3, men4, men5, men6]
    
    def _init_current_men(self):
        return 1
    
    def _init_men_udlr(self):
        return [5, 2, 4, 3]
    
    def _init_move_d(self):
        return 0
    
    def move_dice(self, direction):
        if self._is_east(direction):
            self._move_east()
        if self._is_north(direction):
            self._move_north()
        if self._is_south(direction):
            self._move_south()
        if self._is_west(direction):
            self._move_west()
    
    def _is_east(self, direction):
        return direction == "E"
    def _is_north(self, direction):
        return direction == "N"
    def _is_south(self, direction):
        return direction == "S"
    def _is_west(self, direction):
        return direction == "W"

    def _move_east(self):
        s = self._get_east_value()
        self.men_udlr = self._get_new_udlr_east()
        self.current_men = s

    def _get_east_value(self):
        return self.men_udlr[2]
    
    def _get_new_udlr_east(self):
        return [self.men_udlr[0], self.men_udlr[1],
                7-self.current_men, self.current_men]
    
    def _move_north(self):
        s = self._get_north_value()
        self.men_udlr = self._get_new_udlr_north()
        self.current_men = s
        
    def _get_north_value(self):
        return self.men_udlr[1]
    
    def _get_new_udlr_north(self):
        return [self.current_men, 7-self.current_men,
                self.men_udlr[2], self.men_udlr[3]]
    
    def _move_south(self):
        s = self._get_south_value()
        self.men_udlr = self._get_new_udlr_south()
        self.current_men = s
        
    def _get_south_value(self):
        return self.men_udlr[0]
    
    def _get_new_udlr_south(self):
        return [7-self.current_men, self.current_men,
                self.men_udlr[2], self.men_udlr[3]]
    
    def _move_west(self):
        s = self._get_west_value()
        self.men_udlr = self._get_new_udlr_west()
        self.current_men = s
        
    def _get_west_value(self):
        return self.men_udlr[3]
    
    def _get_new_udlr_west(self):
        return [self.men_udlr[0], self.men_udlr[1],
                self.current_men, 7-self.current_men]
    
    def show_num(self):
        return self._get_current_top_men_value()
    
    def _get_current_top_men_value(self):
        return self.men[self.current_men-1]

main()