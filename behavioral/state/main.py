from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def do_something(self) -> None:
        pass


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.set_state(state)

    def set_state(self, state: State):
        print(f"Context changing to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def do_something(self):
        self._state.do_something()


class ConcreteStateA(State):
    def do_something(self) -> None:
        print("The context is in the state of ConcreteStateA.")
        print("ConcreteStateA now changes the state of the context.")
        self.context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    def do_something(self) -> None:
        print("The context is in the state of ConcreteStateB.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.set_state(ConcreteStateA())


app = Context(ConcreteStateA)
app.do_something()
app.do_something()
