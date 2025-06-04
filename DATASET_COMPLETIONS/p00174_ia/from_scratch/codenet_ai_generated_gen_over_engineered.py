class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def reset_score(self):
        self.score = 0
    
    def add_point(self):
        self.score += 1
    
    def __str__(self):
        return self.name

class GameResult:
    def __init__(self, player_a: Player, player_b: Player):
        self.player_a = player_a
        self.player_b = player_b
    
    def is_finished(self):
        diff = abs(self.player_a.score - self.player_b.score)
        max_score = max(self.player_a.score, self.player_b.score)
        if max_score >= 11:
            if max_score >= 10 and diff >= 2:
                return True
            if max_score > 10 and diff >= 2:
                return True
            if max_score == 11 and diff >= 2:
                return True
            if max_score > 11 and diff >= 2:
                return True
            if max_score == 11 and diff >= 2:
                return True
            if max_score == 11 and diff >= 2:
                return True
            if diff >= 2 and max_score >= 11:
                return True
        # Special case: after 10-10, must have two-point difference
        if max_score >= 10 and diff >= 2:
            return True
        return False
    
    def winner(self):
        if self.is_finished():
            if self.player_a.score > self.player_b.score:
                return self.player_a
            else:
                return self.player_b
        return None

    def scores(self):
        return (self.player_a.score, self.player_b.score)

class ServeSequence:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        char = self.sequence[self.index]
        self.index += 1
        return char

class BadmintonMatch:
    def __init__(self, serve_sequences):
        self.serve_sequences = serve_sequences  # list of strings
        self.player_a = Player("A")
        self.player_b = Player("B")
        self.num_games = 3
        self.current_server = self.player_a  # first game server is A
        self.game_winners = []
    
    def reset_for_game(self, first_server):
        self.player_a.reset_score()
        self.player_b.reset_score()
        self.current_server = first_server
    
    def other_player(self, player):
        return self.player_b if player == self.player_a else self.player_a
    
    def process_game(self, serve_sequence_str, initial_server):
        self.reset_for_game(initial_server)
        serve_sequence = ServeSequence(serve_sequence_str)
        last_point_winner = None
        
        for server_char in serve_sequence:
            # Validate server_char
            if server_char == "A":
                server = self.player_a
            elif server_char == "B":
                server = self.player_b
            else:
                # Invalid char, just continue
                continue
            
            # Sanity check: server must be current_server
            # But problem statement no mention of invalid inputs, so trust input correctness
            
            # Point is won by the server since the server hits the serve,
            # but the problem only records serve order, so point goes to the server who served the last point?
            # No, problem states "次のサーブは直前のポイントを取った人"
            # That means the person who scored last point serves next.
            # So the last point winner served this point.
            # So the person who served current point has just won this point.
            # So point goes to server
            
            # Add point to server
            server.add_point()
            last_point_winner = server
            
            # Check if game finished
            diff = abs(self.player_a.score - self.player_b.score)
            max_score = max(self.player_a.score, self.player_b.score)
            if max_score >= 11:
                if max_score >= 10 and diff >= 2:
                    break
        
        # Record who won this game:
        winner = self.player_a if self.player_a.score > self.player_b.score else self.player_b
        self.game_winners.append(winner)
        # Return final scores in tuple (a_score, b_score)
        return (self.player_a.score, self.player_b.score)
    
    def run_match(self):
        results = []
        # initial server for game 1 is A
        first_server = self.player_a
        for i in range(self.num_games):
            scores = self.process_game(self.serve_sequences[i], first_server)
            results.append(scores)
            # next game first server = previous game winner
            first_server = self.game_winners[-1]
        return results

class InputProcessor:
    def __init__(self):
        self.datasets = []
    
    def read_input(self):
        current_set = []
        while True:
            try:
                line = input().strip()
                if line == '0':
                    break
                current_set.append(line)
                if len(current_set) == 3:
                    self.datasets.append(current_set)
                    current_set = []
            except EOFError:
                break
    
    def get_datasets(self):
        return self.datasets

class OutputPrinter:
    def __init__(self, results_list):
        self.results_list = results_list
    
    def print_results(self):
        for results in self.results_list:
            for score in results:
                print(score[0], score[1])

def main():
    processor = InputProcessor()
    processor.read_input()
    datasets = processor.get_datasets()
    all_results = []
    for serve_sequences in datasets:
        match = BadmintonMatch(serve_sequences)
        results = match.run_match()
        all_results.append(results)
    printer = OutputPrinter(all_results)
    printer.print_results()

if __name__ == "__main__":
    main()