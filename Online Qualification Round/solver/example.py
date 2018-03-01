from .basesolver import BaseSolver


class Solver(BaseSolver):
    """Solve the problem nice and steady!

    !!! This class need to be named 'Solver', otherwise main.py won't find this class.
    """

    def solve(self):
        """Compute a solution to the given problem.

        Save everything in an internal state,
        print the calculated score of the solution.

        :return: True, if a solution is found, False otherwise
        """
        print("Example {} method. Does nothing.".format("->".join([str(self.__class__.__name__), 'solve()'])))
        print("Maybe I should do something with '{}'?".format(self.rides_list))

        return False
