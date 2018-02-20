from .basesolver import BaseSolver


class Solver(BaseSolver):

    def __init__(self, input_str):
        self.input_str = input_str
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), '__init__()'])))
        print("Maybe I should do something with '{}'?".format(input_str))

    def write(self, output_str):
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), 'write()'])))
        print("Maybe I should do something with '{}'?".format(output_str))

    def solve(self):
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), 'solve()'])))
        print("Maybe I should do something with '{}'?".format(self.input_str))
