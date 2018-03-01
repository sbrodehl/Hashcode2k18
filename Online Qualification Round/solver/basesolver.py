import shutil

import numpy as np
from pathlib import Path


class BaseSolver(object):
    """Don't touch this!
    This class makes sure that those two methods gets implemented,
    as needed in main.py.
    """

    def __init__(self, input_str):
        """Initialisation of the given problem.
        """
        self.input_str = input_str

        (self.rows, self.columns, self.vehicles,
         self.rides, self.bonus, self.steps) = 0, 0, 0, 0, 0, 0
        self.rides_list = []
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
        solution_file = Path(output_str)
        prev_fs = solution_file.stat().st_size

        with open(output_str + ".tmp", 'w') as f:
            for sched in self.scheduling:
                f.write(" ".join([str(len(sched))] + [str(i) for i in sched]))
                f.write('\n')

        solution_file_now = Path(output_str + ".tmp")
        now_fs = solution_file_now.stat().st_size

        if now_fs > prev_fs:
            print("Updating solution {} bytes more!!".format(now_fs - prev_fs))
            shutil.move(output_str + ".tmp", output_str)

    @staticmethod
    def _d(t0, t1):
        return np.abs(t0[0] - t1[0]) + np.abs(t0[1] - t1[1])

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.rows, self.columns, self.vehicles, self.rides, self.bonus, self.steps = tuple(
                map(int, first_line.split(' '))
            )

            self.rides_list = []
            for i in range(self.rides):
                self.rides_list.append(tuple(
                    map(int, f.readline().rstrip().split(' '))
                ))
            self.scheduling = [[] for _ in range(self.vehicles)]

        print("Problem statement:")
        print("Map: {}".format((self.rows, self.columns)),
              "Vehicles: {}".format(self.vehicles),
              "Rides: {}".format(self.rides),
              "Bonus: {}".format(self.bonus),
              "Steps: {}".format(self.steps))
