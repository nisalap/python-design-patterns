from state import State
class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def set_state(self, state: State):
        print(f"Context changing to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def do_something(self):
        self._state.do_something()
