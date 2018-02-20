class BaseSolver(object):
    """Don't touch this!
    This class makes sure that those two methods gets implemented,
    as needed in main.py.
    """

    def __init__(self, input_str):
        """Initialisation of the given problem.

        :param input_str: The input filepath to process.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def solve(self):
        """Solves the problem.
        Stores the solution internally.

        :return: Nothing, everything should be save internally.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def write(self, output_str):
        """Writes a solution file with the solved solution.

        :param output_str: The output filepath where to save the solution.
        :return: Nothing.
        """
        raise NotImplementedError("This method needs to be implemented.")
