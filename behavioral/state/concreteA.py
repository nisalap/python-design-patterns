from state import State


class ConcreteStateA(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateA.")
        print("ConcreteStateA now changes the state of the context.")
        self.context.setState(ConcreteStateB())


class ConcreteStateB(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateB.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.setState(ConcreteStateA())