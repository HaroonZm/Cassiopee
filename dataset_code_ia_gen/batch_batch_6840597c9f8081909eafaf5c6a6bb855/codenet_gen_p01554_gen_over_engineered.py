from abc import ABC, abstractmethod
from typing import List, Dict

class AccessState(ABC):
    @abstractmethod
    def toggle(self) -> 'AccessState':
        pass

    @abstractmethod
    def message(self, user_id: str) -> str:
        pass

class LockedState(AccessState):
    def toggle(self) -> 'AccessState':
        return UnlockedState()

    def message(self, user_id: str) -> str:
        return f"Opened by {user_id}"

class UnlockedState(AccessState):
    def toggle(self) -> 'AccessState':
        return LockedState()

    def message(self, user_id: str) -> str:
        return f"Closed by {user_id}"

class UserRegistry:
    def __init__(self, registered_ids: List[str]):
        self._allowed_ids = set(registered_ids)

    def is_registered(self, user_id: str) -> bool:
        return user_id in self._allowed_ids

class DoorController:
    def __init__(self, user_registry: UserRegistry):
        self._user_registry = user_registry
        self._state: AccessState = LockedState()

    def process_access(self, user_id: str) -> str:
        if not self._user_registry.is_registered(user_id):
            return f"Unknown {user_id}"
        self._state = self._state.toggle()
        return self._state.message(user_id)

class InputParser:
    def __init__(self):
        pass

    def parse(self) -> (List[str], List[str]):
        N = int(input())
        registered_ids = [input().strip() for _ in range(N)]
        M = int(input())
        access_attempts = [input().strip() for _ in range(M)]
        return registered_ids, access_attempts

class OutputHandler:
    def __init__(self):
        pass

    def output_messages(self, messages: List[str]) -> None:
        for message in messages:
            print(message)

class KagisysSystem:
    def __init__(self):
        self._parser = InputParser()
        self._output = OutputHandler()

    def run(self) -> None:
        registered_ids, access_attempts = self._parser.parse()

        user_registry = UserRegistry(registered_ids)
        door_controller = DoorController(user_registry)

        results = []
        for user_id in access_attempts:
            results.append(door_controller.process_access(user_id))

        self._output.output_messages(results)

if __name__ == "__main__":
    KagisysSystem().run()