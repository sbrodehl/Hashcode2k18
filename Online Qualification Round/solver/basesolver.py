class BaseSolver(object):
    """Don't touch this!
    This class makes sure that those two methods gets implemented,
    as needed in main.py.
    """

    def __init__(self, input_str):
        """Initialisation of the given problem.
        """
        self.input_str = input_str

        self.drive_count = 0
        self.rides = []
        self.scheduling = []
        self.read_input()

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

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            R, C, F, N, B, T = tuple(
                map(int, first_line.split(' '))
            )

            self.rides = []
            for i in range(N):
                self.rides.append(tuple(
                    map(int, f.readline().rstrip().split(' '))
                ))

        print("Problem statement:")
        print(R, C, F, N, B, T)
        print(self.rides)
