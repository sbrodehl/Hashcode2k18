from .basesolver import BaseSolver

import numpy as np


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
        time = 0
        start = (0, 0)
        ride_taken = np.zeros(self.rides)
        cars = [{'pos': (0, 0), 'avail': True} for _ in range(self.vehicles)]
        for cidx, car in enumerate(cars):
            diffs = np.zeros(self.rides, np.int32)
            diffs[:] = np.iinfo(np.int32).max
            for ridx, ride in enumerate(self.rides_list):
                if ride_taken[ridx]:
                    continue
                d_to_car = self._d(car['pos'], (ride[0], ride[1]))
                if d_to_car + time > self.steps:
                    continue
                es = ride[4] - time
                diffs[ridx] = np.abs(self._d(car['pos'], start) - es)
            # get min
            choosen = np.argmin(diffs)
            ride_taken[choosen] = 1
            car['avail'] = False
            self.scheduling[cidx].append(choosen)

        # run simulation
        while time < self.steps:
            for cidx, car in enumerate(cars):
                pass
            time += 1

        return True

    @staticmethod
    def _d(t0, t1):
        return np.abs(t0[0] - t1[0]) + np.abs(t0[1] - t1[1])
