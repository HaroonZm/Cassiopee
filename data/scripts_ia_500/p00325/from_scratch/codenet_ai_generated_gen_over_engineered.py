from collections import deque
from typing import List, Dict, Union, Optional, Tuple, Set

class Variable:
    def __init__(self, name: str) -> None:
        self.name = name
        self.value: int = 0

    def set_value(self, val: int) -> bool:
        if 0 <= val < 16:
            self.value = val
            return True
        else:
            return False

    def __lt__(self, other: 'Variable') -> bool:
        return self.name < other.name

class Instruction:
    def __init__(self, line: int) -> None:
        self.line = line
    
    def execute(self, context: 'ExecutionContext') -> Optional[int]:
        """Executes instruction, returns next line to execute or None if normal flow"""
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(line={self.line})"

class AddVarVar(Instruction):
    def __init__(self, line: int, dst: str, src1: str, src2: str) -> None:
        super().__init__(line)
        self.dst = dst
        self.src1 = src1
        self.src2 = src2

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        v1 = ctx.get_var_value(self.src1)
        v2 = ctx.get_var_value(self.src2)
        res = v1 + v2
        if not ctx.set_var_value(self.dst, res):
            return -1  # Halt condition
        return None

class AddVarConst(Instruction):
    def __init__(self, line: int, dst: str, src: str, con: int) -> None:
        super().__init__(line)
        self.dst = dst
        self.src = src
        self.con = con

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        v = ctx.get_var_value(self.src)
        res = v + self.con
        if not ctx.set_var_value(self.dst, res):
            return -1
        return None

class SubVarVar(Instruction):
    def __init__(self, line: int, dst: str, src1: str, src2: str) -> None:
        super().__init__(line)
        self.dst = dst
        self.src1 = src1
        self.src2 = src2

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        v1 = ctx.get_var_value(self.src1)
        v2 = ctx.get_var_value(self.src2)
        res = v1 - v2
        if not ctx.set_var_value(self.dst, res):
            return -1
        return None

class SubVarConst(Instruction):
    def __init__(self, line: int, dst: str, src: str, con: int) -> None:
        super().__init__(line)
        self.dst = dst
        self.src = src
        self.con = con

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        v = ctx.get_var_value(self.src)
        res = v - self.con
        if not ctx.set_var_value(self.dst, res):
            return -1
        return None

class SetVarVar(Instruction):
    def __init__(self, line: int, dst: str, src: str) -> None:
        super().__init__(line)
        self.dst = dst
        self.src = src

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        v = ctx.get_var_value(self.src)
        if not ctx.set_var_value(self.dst, v):
            return -1
        return None

class SetVarConst(Instruction):
    def __init__(self, line: int, dst: str, con: int) -> None:
        super().__init__(line)
        self.dst = dst
        self.con = con

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        if not ctx.set_var_value(self.dst, self.con):
            return -1
        return None

class IfInstruction(Instruction):
    def __init__(self, line: int, var_name: str, dest: int) -> None:
        super().__init__(line)
        self.var_name = var_name
        self.dest = dest

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        val = ctx.get_var_value(self.var_name)
        if val != 0:
            if self.dest not in ctx.program.lines_index:
                # jump to nonexistent line => halt
                return -1
            return self.dest
        return None

class HaltInstruction(Instruction):
    def __init__(self, line: int) -> None:
        super().__init__(line)

    def execute(self, ctx: 'ExecutionContext') -> Optional[int]:
        return -1  # special halt signal

class Program:
    def __init__(self, instructions: List[Instruction]) -> None:
        # Map line number to instruction and maintain order
        self.instructions = instructions
        self.lines_index: Dict[int, int] = {inst.line: idx for idx, inst in enumerate(instructions)}
        self.sorted_lines = sorted(self.lines_index.keys())

    def next_line(self, current_line: int) -> Optional[int]:
        # Return line number next to current_line in program order, or None if none
        idx = self.lines_index[current_line]
        if idx + 1 < len(self.instructions):
            return self.instructions[idx+1].line
        return None

    def get_instruction(self, line: int) -> Instruction:
        return self.instructions[self.lines_index[line]]


class ExecutionContext:
    def __init__(self, program: Program) -> None:
        self.program = program
        self.vars: Dict[str,int] = {}
        self.vars_seen: Set[str] = set()
        self.vars_limit = 5  # at most 5 different variables possible
        self.visited: Set[Tuple[int,Tuple[Tuple[str,int],...]]] = set()
        self.MAX_EXECUTIONS = 100_000  # fail-safe, but primary detection is via visited states

    def get_var_value(self, var: str) -> int:
        if var not in self.vars:
            if len(self.vars) >= self.vars_limit:
                # Should not occur per problem statement
                self.vars[var] = 0
            else:
                self.vars[var] = 0
            self.vars_seen.add(var)
        return self.vars[var]

    def set_var_value(self, var: str, val: int) -> bool:
        # Returns True if allowed, False if would halt (val < 0 or val >= 16)
        if var not in self.vars:
            if len(self.vars) < self.vars_limit:
                self.vars[var] = 0
            else:
                # not expected per problem constraints
                self.vars[var] = 0
            self.vars_seen.add(var)
        if 0 <= val < 16:
            self.vars[var] = val
            return True
        else:
            # halting condition: negative or >= 16 assignment disallowed
            return False

    def state_tuple(self, line: int) -> Tuple[int, Tuple[Tuple[str,int], ...]]:
        # Return immutable state representation for visited check
        vars_sorted = tuple(sorted(self.vars.items()))
        return (line, vars_sorted)

class HaltingAnalyzer:
    def __init__(self, program: Program) -> None:
        self.program = program
        self.ctx = ExecutionContext(program)

    def analyze(self) -> Union[str, Dict[str,int]]:
        # Executes and analyzes if halts or loops
        # Use DFS with memoization on (line, variables) states to detect loops

        stack: List[Tuple[int, Dict[str,int]]] = []
        visited_states: Set[Tuple[int, Tuple[Tuple[str,int], ...]]] = set()

        # Work queue contains tuples: (line to execute, variables state)
        from collections import deque
        queue = deque()

        # Start from first instruction line
        start_line = self.program.sorted_lines[0]
        start_vars = {v:0 for v in self.ctx.vars_seen}  # empty initially, will add in run
        # To allow vars to build, start from empty dict
        queue.append( (start_line, dict()) )
        
        # We'll do iterative DFS traversal to detect loops, but must cap big state spaces.
        # Because variables max 5 and values 0..15 at most, possible states are bounded.
        # State space size maximally ~50 (lines) * 16^5 (variables) ~ huge but we limit by real appearance.

        while queue:
            line, vars_state = queue.pop()

            vars_key_sorted = tuple(sorted(vars_state.items()))
            state_key = (line, vars_key_sorted)
            if state_key in visited_states:
                continue
            visited_states.add(state_key)

            if line not in self.program.lines_index:
                # Jump to nonexistent line => halt here
                # Save variables state for output
                return vars_state

            inst = self.program.get_instruction(line)

            # Setup ctx vars for this run
            self.ctx.vars = dict(vars_state)
            # Also update vars_seen to include any variable appeared in program for output
            for v in self.program.variables_in_program:
                if v not in self.ctx.vars:
                    self.ctx.vars[v] = 0
            
            res = inst.execute(self.ctx)
            if res == -1:
                # Halt reached or illegal assignment or invalid jump
                # Halt immediately, output current vars
                return self.ctx.vars
            elif res is None:
                # normal next line
                nline = self.program.next_line(line)
                if nline is None:
                    # last statement, normal halt condition
                    return self.ctx.vars
                queue.append( (nline, dict(self.ctx.vars)) )
            else:
                # Jump to res line
                queue.append( (res, dict(self.ctx.vars)) )
        
        # If exit loop not by return, means infinite execution
        return "inf"


class ProgramParser:
    @staticmethod
    def parse_line(line: str) -> Instruction:
        parts = line.strip().split()
        line_no = int(parts[0])
        op = parts[1]

        if op == 'ADD':
            _, _, dst, src2, src3 = parts
            if src3.isalpha():
                # ADD var1 var2 var3
                return AddVarVar(line_no, dst, src2, src3)
            else:
                # ADD var1 var2 con
                con = int(src3)
                return AddVarConst(line_no, dst, src2, con)
        elif op == 'SUB':
            _, _, dst, src2, src3 = parts
            if src3.isalpha():
                return SubVarVar(line_no, dst, src2, src3)
            else:
                con = int(src3)
                return SubVarConst(line_no, dst, src2, con)
        elif op == 'SET':
            _, _, dst, src = parts
            if src.isalpha():
                return SetVarVar(line_no, dst, src)
            else:
                con = int(src)
                return SetVarConst(line_no, dst, con)
        elif op == 'IF':
            _, _, var, dest = parts
            dest_line = int(dest)
            return IfInstruction(line_no, var, dest_line)
        elif op == 'HALT':
            return HaltInstruction(line_no)
        else:
            raise ValueError(f"Unknown operation {op}")

class TinyPowerProgram(Program):
    def __init__(self, instructions: List[Instruction]) -> None:
        super().__init__(instructions)
        self.variables_in_program = self.find_variables()

    def find_variables(self) -> Set[str]:
        vars_set = set()
        for inst in self.instructions:
            if isinstance(inst, (AddVarVar, AddVarConst, SubVarVar, SubVarConst, SetVarVar, SetVarConst, IfInstruction)):
                # Collect variables used
                # For AddVarVar / SubVarVar
                if hasattr(inst, 'dst'): vars_set.add(inst.dst)
                if hasattr(inst, 'src'): 
                    if isinstance(inst.src, str) and inst.src.isalpha():
                        vars_set.add(inst.src)
                if hasattr(inst, 'src1'):
                    if inst.src1.isalpha():
                        vars_set.add(inst.src1)
                if hasattr(inst, 'src2'):
                    if inst.src2.isalpha():
                        vars_set.add(inst.src2)
                if hasattr(inst, 'var_name'):
                    vars_set.add(inst.var_name)
            # HALT has no variable
        return vars_set


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    insts: List[Instruction] = []
    for _ in range(N):
        line = input().rstrip('\n')
        inst = ProgramParser.parse_line(line)
        insts.append(inst)
    program = TinyPowerProgram(insts)
    
    analyzer = HaltingAnalyzer(program)
    result = analyzer.analyze()

    if result == "inf":
        print("inf")
        return
    else:
        # result is dict variable => int
        # ensure variables in lex order from program variables or keys in result
        vars_all = set(result.keys()) | program.variables_in_program
        vars_out = sorted(vars_all)
        for var in vars_out:
            val = result.get(var, 0)
            print(f"{var}={val}")

if __name__=="__main__":
    main()