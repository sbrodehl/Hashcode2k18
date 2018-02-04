class BaseSolver(object):
    """Don't touch this!
    This class makes sure that those two methods gets implemented,
    as needed in main.py.
    """

    def __init__(self):
        """Initialisation of the given problem.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def solve(self):
        """Solves the problem.
        Stores the solution internally.

        :return: True, if a solution is found, False otherwise
        """
        raise NotImplementedError("This method needs to be implemented.")

    def write(self, output_str):
        """Writes a solution file with the solved solution.

        :param output_str: The output filepath where to save the solution.
        :return: Nothing.
        """
        raise NotImplementedError("This method needs to be implemented.")
