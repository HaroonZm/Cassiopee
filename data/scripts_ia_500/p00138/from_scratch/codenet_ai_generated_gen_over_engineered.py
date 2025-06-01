from typing import List, Tuple
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class Athlete:
    time: float
    number: int = field(compare=False)
    heat: int = field(compare=False)

class Heat:
    def __init__(self, heat_id: int, athletes: List[Athlete]):
        self.heat_id = heat_id
        # Sort athletes by time ascendingly
        self.athletes = sorted(athletes)
        
    def get_top_two(self) -> List[Athlete]:
        # Return first and second place athletes
        return self.athletes[:2]
    
    def get_remaining(self) -> List[Athlete]:
        # Return athletes below 2nd place
        return self.athletes[2:]

class Championship:
    def __init__(self, heats: List[Heat]):
        self.heats = heats
    
    def select_finalists(self) -> List[Athlete]:
        finalists = []
        leftovers = []
        
        # Get top 2 from each heat
        for heat in self.heats:
            finalists.extend(heat.get_top_two())
            leftovers.extend(heat.get_remaining())
            
        # Select next 2 best from leftovers
        leftovers.sort()
        finalists.extend(leftovers[:2])
        
        return finalists

class InputParser:
    def __init__(self, raw_lines: List[str]):
        self.raw_lines = raw_lines
    
    def parse(self) -> Championship:
        # 24 lines, 3 heats of 8 athletes
        athletes_per_heat = 8
        heats = []
        for i in range(3):
            athletes = []
            for j in range(athletes_per_heat):
                idx = i*athletes_per_heat + j
                line = self.raw_lines[idx].strip()
                p_str, t_str = line.split()
                p = int(p_str)
                t = float(t_str)
                athlete = Athlete(time=t, number=p, heat=i+1)
                athletes.append(athlete)
            heat = Heat(i+1, athletes)
            heats.append(heat)
        return Championship(heats)

class OutputFormatter:
    def __init__(self, championship: Championship):
        self.championship = championship
        
    def format(self) -> List[str]:
        finalists = self.championship.select_finalists()
        # We must output in order:
        # 1 heat's top 2
        # 2 heat's top 2
        # 3 heat's top 2
        # then two fastest from leftovers

        # Group finalists by heat
        by_heat = {1:[], 2:[],3:[]}
        leftovers = []
        for athlete in finalists:
            if len(by_heat[athlete.heat]) < 2:
                by_heat[athlete.heat].append(athlete)
            else:
                leftovers.append(athlete)  # two best leftovers
                
        lines = []
        # Add top 2 from each heat in heat order
        for heat_id in [1, 2, 3]:
            # sort just in case
            heat_athletes = sorted(by_heat[heat_id])
            for a in heat_athletes:
                lines.append(f"{a.number} {a.time:.2f}")
        # Add leftovers sorted by time
        leftovers = sorted(leftovers)
        for a in leftovers:
            lines.append(f"{a.number} {a.time:.2f}")
        return lines

def main():
    import sys
    lines = [sys.stdin.readline() for _ in range(24)]
    parser = InputParser(lines)
    championship = parser.parse()
    formatter = OutputFormatter(championship)
    result_lines = formatter.format()
    for line in result_lines:
        print(line)

if __name__ == "__main__":
    main()