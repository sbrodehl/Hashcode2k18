from .basesolver import BaseSolver


class Solver(BaseSolver):
    """Solve the problem nice and steady!

    !!! This class need to be named 'Solver', otherwise main.py won't find this class.
    """
    def __init__(self, input_str):
        """Initialise the problem,
        e.g. - read the input,
             - preprocess data,
             - build heuristics,
             - ...
        """
        self.input_str = input_str
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), '__init__()'])))
        print("Maybe I should do something with '{}'?".format(input_str))

    def write(self, output_str):
        """Write the computed solution to the give filepath.
        If no solution was previously computed, nothing is done.

        :param output_str: The filepath where to save the solution.
        :return: True, if the solution is saved, False otherwise.
        """
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), 'write()'])))
        print("Maybe I should do something with '{}'?".format(output_str))

        return False

    def solve(self):
        """Compute a solution to the given problem.

        Save everything in an internal state,
        print the calculated score of the solution.

        :return: True, if a solution is found, False otherwise
        """
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), 'solve()'])))
        print("Maybe I should do something with '{}'?".format(self.input_str))

        return False
