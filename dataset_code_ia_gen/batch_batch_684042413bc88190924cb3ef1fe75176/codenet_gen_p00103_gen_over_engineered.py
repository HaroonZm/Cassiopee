class Base( object ):
    """Abstract representation of a base in baseball."""
    def __init__( self ):
        self.next_base = None
        self.runner = False

    def set_next_base( self, base ):
        self.next_base = base

    def has_runner( self ):
        return self.runner

    def set_runner( self, val ):
        self.runner = val

    def advance_runner( self ):
        """
        Move runner from this base to the next base.
        If next base is None, it means home plate reached - return True for run scored.
        """
        if self.runner:
            if self.next_base is None:
                self.runner = False
                return True
            if not self.next_base.has_runner():
                self.next_base.set_runner( True )
                self.runner = False
                return False
            # If next base already occupied, recursively advance the runner on next base first
            runs_scored = self.next_base.advance_runner()
            self.next_base.set_runner( True )
            self.runner = False
            return runs_scored
        return False


class BasesManager( object ):
    """
    Manage all bases, their runners, and advancing logic.
    Uses a linked structure: First -> Second -> Third -> None (home)
    """
    def __init__( self ):
        self.first = Base()
        self.second = Base()
        self.third = Base()
        self.first.set_next_base( self.second )
        self.second.set_next_base( self.third )
        self.third.set_next_base( None )  # null next base = home plate

    def add_runner_on_first( self ):
        """
        Add a runner on first base.
        If first base is occupied, advance runner(s) accordingly before adding.
        """
        # Advance existing runners starting from third to home if needed to make room
        if self.first.has_runner():
            runs_from_advance = self.first.advance_runner()
            # if someone scored during advancement, we need to track it from outside
            # for this logic, return runs scored
            return runs_from_advance
        self.first.set_runner( True )
        return 0

    def advance_all_runners( self ):
        """
        Advance all runners by one base (used for HIT event)
        Runners on third base score.
        Return the number of runs scored.
        """
        runs = 0
        # We advance runners on third first (to score)
        if self.third.has_runner():
            runs += 1
            self.third.set_runner( False )
        # Move runners on second to third
        if self.second.has_runner():
            self.second.set_runner( False )
            self.third.set_runner( True )
        # Move runners on first to second
        if self.first.has_runner():
            self.first.set_runner( False )
            self.second.set_runner( True )
        # Finally set new runner on first base
        self.first.set_runner( True )
        return runs

    def all_runners_score_and_clear( self ):
        """
        For HOMERUN event:
        Count all runners on bases plus the batter,
        clear all bases,
        return total runs scored.
        """
        runners_count = sum( [ 1 if base.has_runner() else 0 for base in [self.first, self.second, self.third] ] )
        total_runs = runners_count + 1  # batter also scores
        self.first.set_runner( False )
        self.second.set_runner( False )
        self.third.set_runner( False )
        return total_runs

    def __str__( self ):
        """Debug state for units tests or logs."""
        return f"Bases: 1st: {self.first.has_runner()}, 2nd: {self.second.has_runner()}, 3rd: {self.third.has_runner()}"


class Inning( object ):
    """
    Representation of an inning simulation.
    Tracks outs, bases, and score.
    """
    MAX_OUTS = 3

    def __init__( self ):
        self.bases_manager = BasesManager()
        self.outs = 0
        self.score = 0
        self.ended = False

    def process_event( self, event ):
        """
        Process a single event and update the inning state.
        Returns True if inning ended due to 3 outs, else False.
        """
        if self.ended:
            # Inning already ended, ignore further events
            return True

        event = event.strip()

        if event == "HIT":
            runs_scored = self.bases_manager.advance_all_runners()
            self.score += runs_scored
        elif event == "HOMERUN":
            runs_scored = self.bases_manager.all_runners_score_and_clear()
            self.score += runs_scored
        elif event == "OUT":
            self.outs += 1
            if self.outs >= self.MAX_OUTS:
                self.ended = True
        else:
            raise ValueError( f"Unknown event: {event}" )
        return self.ended


class BaseballSimulation( object ):
    """
    Orchestrator for multiple innings/datasets and input/output handling.
    This abstraction anticipates future expansions like multiple innings, teams, etc.
    """
    def __init__( self ):
        self.innings = []

    def read_input( self, lines ):
        """
        Parses input lines to populate innings.
        Input format:
        - First line: number of datasets n
        - Next lines: events per inning (unknown number per inning; until 3 outs or eof).
        This parser expects events for each inning to be given line by line until 3 outs are reached.
        """
        n = int( lines[0].strip() )
        idx = 1
        for _ in range( n ):
            inning = Inning()
            while idx < len(lines) and not inning.ended:
                line = lines[idx].strip()
                if line == '':
                    idx += 1
                    continue
                inning.process_event( line )
                idx += 1
            self.innings.append( inning )

    def get_scores( self ):
        """Return a list of scores for all innings processed."""
        return [ inning.score for inning in self.innings ]


def main():
    import sys
    input_lines = [ line for line in sys.stdin ]
    sim = BaseballSimulation()
    sim.read_input( input_lines )
    scores = sim.get_scores()
    for score in scores:
        print( score )


if __name__ == "__main__":
    main()