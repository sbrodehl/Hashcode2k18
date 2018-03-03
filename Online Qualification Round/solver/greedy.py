from .basesolver import BaseSolver

import numpy as np
from random import randint
from tqdm import tqdm


class Solver(BaseSolver):
    """Randomly choose a vehicle for every ride, once.

    Spoiler alter: works quite fast, scores quite low.
    """

    def solve(self):
        """Compute a solution to the given problem.

        Save everything in an internal state,
        print the calculated score of the solution.

        :return: True, if a solution is found, False otherwise
        """
        time_table = np.zeros(shape=(self.vehicles, self.steps), dtype=np.uint8)
        veh_pos = []
        veh_rid_id = []
        for _ in range(self.vehicles):
            l = []
            ll = []
            for _ in range(self.steps):
                l.append((0, 0))
                ll.append(-1)
            veh_pos.append(l)
            veh_rid_id.append(ll)

        del l, ll

        pbar = tqdm(total=len(self.rides_list))
        for idx, ride in enumerate(self.rides_list):
            pbar.update(1)
            six, siy, fix, fiy, es, lf = ride
            ride_start = (six, siy)
            ride_end = (fix, fiy)

            drive_len = self._d(ride_start, ride_end)
            for cccaaaar in range(10):
                # choose random car
                rnd_veh = randint(0, self.vehicles - 1)
                veh_sched = time_table[rnd_veh]
                car_pos = veh_pos[rnd_veh]

                # choose earliest avail start time
                # maybe randomize this
                car_avail_t = np.where(veh_sched == 0)[0][0]

                d_to_ride = self._d(car_pos[car_avail_t], ride_start)

                # if we need to wait, start later
                if (car_avail_t + d_to_ride) - es > 0:
                    car_avail_t += (car_avail_t + d_to_ride) - es

                # ###
                start = car_avail_t
                trip_len = d_to_ride + drive_len
                # check for in time delivery
                if lf < start + trip_len:
                    continue

                ones = np.ones(shape=(trip_len,))
                cache = veh_sched[start: start + trip_len]
                veh_sched[start: start + trip_len] = np.add(veh_sched[start: start + trip_len], ones)

                # sanity check for over booking
                if np.max(veh_sched) > 1:
                    veh_sched[start: start + trip_len] = cache
                    continue

                car_pos[start + trip_len] = ride_end
                veh_rid_id[rnd_veh][start: start + trip_len] = [idx] * trip_len
                break

        # reduce ids for solution
        for idx in range(self.vehicles):
            lastel = -1
            for iiiiddddxx in veh_rid_id[idx]:
                if iiiiddddxx >= 0 and iiiiddddxx != lastel:
                    self.scheduling[idx].append(iiiiddddxx)
                    lastel = iiiiddddxx

        return True
