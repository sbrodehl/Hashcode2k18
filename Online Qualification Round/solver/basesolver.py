import numpy as np
import json

from .score import Car, Score, Ride, check_ride_ids, check_vehicles, eval_ride


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
        self.score = 0
        self.rides_list = []
        self.scheduling = []
        self.read_input()
        self.json = {
            "row": self.rows,
            "column": self.columns,
            "rides": []
        }

    def solve(self):
        """Solves the problem.
        Stores the solution internally.

        :return: True, if a solution is found, False otherwise
        """
        raise NotImplementedError("This method needs to be implemented.")

    def compute_score(self):
        """Validates submission and computes score.

        :return: the computed score of the given scheduling
        """
        if check_vehicles(self.vehicles, len(self.scheduling)):
            print("vehicles: OK")
        if check_ride_ids(self.scheduling, self.rides):
            print("ride ids: OK")

        ride_taken = []
        score = Score()
        for vehicle_rides in self.scheduling:
            car = Car()
            ride_taken.extend(vehicle_rides)
            for rid in vehicle_rides:
                r = self.rides_list[rid]
                ride = Ride(rid, *r)
                code = eval_ride(car, ride, score, self.bonus, self.steps)
                self.json["rides"].append([ride.x1, ride.y1, ride.x2, ride.y2, code])
        score.unassigned = self.rides - score.taken

        ride_taken = set(ride_taken)
        missed = set(range(self.rides)) - ride_taken
        for m in missed:
            r = self.rides_list[m]
            self.json["rides"].append([r[0], r[1], r[2], r[3], -1])

        self.score = score.total()
        return self.score

    def write(self, output_str):
        """Writes a solution file with the solved solution.

        :param output_str: The output filepath where to save the solution.
        :return: Nothing.
        """
        self.compute_score()
        print(self.score)
        with open(output_str, 'w') as f:
            for sched in self.scheduling:
                f.write(" ".join([str(len(sched))] + [str(i) for i in sched]))
                f.write('\n')
        with open(output_str + ".json", 'w') as f:
            json.dump(self.json, f)

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
