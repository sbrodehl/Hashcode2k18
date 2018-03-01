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
        ride_taken = np.zeros(self.rides)
        on_mission = np.zeros(shape=(self.vehicles, self.steps), dtype=np.uint8)
        cars = [{'pos': (0, 0)} for _ in range(self.vehicles)]

        # run simulation
        while time < self.steps:

            for cidx, car in enumerate(cars):
                if on_mission[cidx][time]:
                    continue
                rpriority = np.zeros(self.rides, np.int32)
                rpriority[:] = np.iinfo(np.int32).max
                fail_early = True
                for ridx, ride in enumerate(self.rides_list):
                    if ride_taken[ridx]:
                        continue
                    d_to_car = self._d(car['pos'], (ride[0], ride[1]))
                    # sanity check, if ride is reachable in time
                    if time + d_to_car > self.steps:
                        continue
                    # check if ride can be finished in time
                    ride_len = self._d((ride[0], ride[1]), (ride[2], ride[3]))
                    if time + d_to_car + ride_len > ride[5]:
                        continue
                    es = ride[4] - time
                    rpriority[ridx] = np.abs(d_to_car - es)
                    fail_early = False
                # check if at least one ride is available
                if fail_early:
                    continue
                # get min
                ridx = np.argmin(rpriority)
                ride = self.rides_list[ridx]
                ride_taken[ridx] = 1
                ride_start = (ride[0], ride[1])
                ride_end = (ride[2], ride[3])
                d_to_car = self._d(car['pos'], ride_start)
                ride_len = self._d(ride_start, ride_end)
                ers = np.max([time + d_to_car, ride[4]])
                on_mission[cidx][time: ers + ride_len] = np.ones(shape=(ers + ride_len - time,))
                self.scheduling[cidx].append(ridx)
                car['pos'] = ride_end

            time += 1

        return True

    @staticmethod
    def _d(t0, t1):
        return np.abs(t0[0] - t1[0]) + np.abs(t0[1] - t1[1])
