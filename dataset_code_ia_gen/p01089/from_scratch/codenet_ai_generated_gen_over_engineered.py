from typing import List, Set, Dict, Tuple
from abc import ABC, abstractmethod


class Instruction(ABC):
    @abstractmethod
    def execute(self, thread: "Thread", lock_manager: "LockManager") -> bool:
        """
        Attempt to execute this instruction by the given thread with the given lock manager.
        Return True if executed successfully, False if blocked.
        """
        pass


class AcquireLockInstruction(Instruction):
    def __init__(self, lock_id: int):
        self.lock_id = lock_id

    def execute(self, thread: "Thread", lock_manager: "LockManager") -> bool:
        if lock_manager.is_free(self.lock_id):
            lock_manager.acquire(self.lock_id, thread)
            thread.advance()
            return True
        else:
            # lock is already held by some thread; cannot acquire now
            return False


class ReleaseAllLocksInstruction(Instruction):
    def execute(self, thread: "Thread", lock_manager: "LockManager") -> bool:
        lock_manager.release_all(thread)
        thread.advance()
        return True


class InstructionFactory:
    @staticmethod
    def from_char(c: str) -> Instruction:
        if c == 'u':
            return ReleaseAllLocksInstruction()
        else:
            return AcquireLockInstruction(int(c))


class Thread:
    def __init__(self, instr_sequence: List[Instruction]):
        self.instr_sequence: List[Instruction] = instr_sequence
        self.pc: int = 0  # program counter
        self.held_locks: Set[int] = set()
        self.finished: bool = False

    def current_instruction(self) -> Instruction:
        if self.pc < len(self.instr_sequence):
            return self.instr_sequence[self.pc]
        else:
            return None

    def advance(self) -> None:
        self.pc += 1
        if self.pc == len(self.instr_sequence):
            self.finished = True


class LockManager:
    def __init__(self):
        # Map from lock_id to thread that currently holds it, or None if free
        self.lock_owners: Dict[int, Thread] = {k: None for k in range(10)}

    def is_free(self, lock_id: int) -> bool:
        return self.lock_owners[lock_id] is None

    def acquire(self, lock_id: int, thread: Thread) -> None:
        self.lock_owners[lock_id] = thread
        thread.held_locks.add(lock_id)

    def release_all(self, thread: Thread) -> None:
        for lock_id in list(thread.held_locks):
            self.lock_owners[lock_id] = None
            thread.held_locks.remove(lock_id)


class DeadlockDetector:
    THREAD_COUNT = 10

    def __init__(self, instr_sequence: List[Instruction]):
        self.instr_sequence: List[Instruction] = instr_sequence
        self.threads: List[Thread] = [Thread(instr_sequence) for _ in range(self.THREAD_COUNT)]
        self.lock_manager: LockManager = LockManager()

    def is_deadlock_possible(self) -> bool:
        """
        We model the problem of potential deadlock by simulating all
        possible progressions that different scheduling choices
        might produce, looking if some leads to deadlock.

        To avoid brute force exponential explosion, we model the system state
        in terms of:
         - each thread's program counter
         - which locks are held and by which thread

        If we reach a state where all unfinished threads have next instruction 
        blocked on held locks, it's a deadlock.

        We use BFS with memoization, and stop if we detect a deadlock state.
        """
        from collections import deque

        State = Tuple[Tuple[int, ...], Tuple[Tuple[int, int], ...]]
        # Thread PCs as tuple
        # Lock owners as tuple (lock_id, owner_thread_index) for locks held, sorted asc

        def serialize_state(threads: List[Thread], lock_manager: LockManager) -> State:
            pcs = tuple(t.pc for t in threads)
            owners = []
            for lock_id, owner in lock_manager.lock_owners.items():
                if owner is not None:
                    owners.append((lock_id, threads.index(owner)))
            owners.sort()
            return (pcs, tuple(owners))

        initial_state = serialize_state(self.threads, self.lock_manager)
        visited = set()
        visited.add(initial_state)

        queue = deque()
        queue.append((self.threads, self.lock_manager))

        while queue:
            current_threads, current_lock_manager = queue.popleft()

            # Check if all threads finished
            if all(t.finished for t in current_threads):
                # All finished safely
                continue

            # Find all threads that can execute their next instruction without blocking
            executable_threads = []
            for idx, thread in enumerate(current_threads):
                if thread.finished:
                    continue
                instr = thread.current_instruction()
                if isinstance(instr, AcquireLockInstruction):
                    if current_lock_manager.is_free(instr.lock_id):
                        executable_threads.append(idx)
                elif isinstance(instr, ReleaseAllLocksInstruction):
                    # always executable
                    executable_threads.append(idx)

            if not executable_threads:
                # No thread can execute next instruction, but some unfinished -> deadlock
                return True

            # Try all possible next moves and enqueue new states
            for th_idx in executable_threads:
                # Deep copy current state
                new_threads = []
                for t in current_threads:
                    copy_t = Thread(self.instr_sequence)
                    copy_t.pc = t.pc
                    copy_t.finished = t.finished
                    copy_t.held_locks = set(t.held_locks)
                    new_threads.append(copy_t)
                new_lock_manager = LockManager()
                # copy lock ownership
                for lock_id, owner_thread in current_lock_manager.lock_owners.items():
                    if owner_thread is not None:
                        # locate owner index in old state and get corresponding thread in new state
                        owner_idx = current_threads.index(owner_thread)
                        new_lock_manager.lock_owners[lock_id] = new_threads[owner_idx]
                # Now execute chosen thread's next instruction
                chosen_thread = new_threads[th_idx]
                instr = chosen_thread.current_instruction()
                executed = instr.execute(chosen_thread, new_lock_manager)
                # executed must be True because it was in executable_threads
                new_state = serialize_state(new_threads, new_lock_manager)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_threads, new_lock_manager))

        # exhaustively explored all without deadlock
        return False


class InputParser:
    @staticmethod
    def parse_input_line(n: int, s: str) -> List[Instruction]:
        instrs = []
        for c in s:
            instr = InstructionFactory.from_char(c)
            instrs.append(instr)
        return instrs


class DeadlockDetectionProgram:
    def __init__(self):
        pass

    def run(self):
        import sys
        lines = sys.stdin.read().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if line == '0':
                break
            n = int(line)
            s = lines[i].strip()
            i += 1
            instr_sequence = InputParser.parse_input_line(n, s)
            detector = DeadlockDetector(instr_sequence)
            unsafe = detector.is_deadlock_possible()
            print("UNSAFE" if unsafe else "SAFE")


if __name__ == "__main__":
    DeadlockDetectionProgram().run()