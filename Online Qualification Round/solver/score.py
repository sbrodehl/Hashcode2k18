#! /usr/bin/python3

"""
author: https://github.com/PicoJr

https://github.com/PicoJr/2018-hashcode-score/blob/9d0345b12ca7a39553681bd14047ec5cdc814971/score.py
"""

import argparse
import logging


def d(x1, y1, x2, y2):
    """Manhattan distance between (x1,y1) and (x2,y2)"""
    return abs(x2 - x1) + abs(y2 - y1)


class Score(object):
    def __init__(self):
        self.raw_score = 0
        self.bonus_score = 0  # points obtained from bonus
        self.taken = 0  # arrival in time
        self.unassigned = 0
        self.late = 0  # late arrival
        self.bonus = 0  # departure on time
        self.wait_time = 0  # total wait time

    def total(self):
        return self.raw_score + self.bonus_score


class Ride(object):
    def __init__(self, rid, x1, y1, x2, y2, step_min, step_max):
        self.rid = rid
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.step_min = step_min
        self.step_max = step_max

    def distance(self):
        return d(self.x1, self.y1, self.x2, self.y2)


class Car(object):
    def __init__(self):
        self.assigned_rides = []
        self.step = 0
        self.x = 0
        self.y = 0

    def distance_to(self, x, y):
        return d(self.x, self.y, x, y)

    def distance_to_ride_start(self, ride):
        return d(self.x, self.y, ride.x1, ride.y1)

    def wait_time(self, ride):
        return max(0, ride.step_min - (self.step + self.distance_to_ride_start(ride)))

    def arrival(self, ride):
        return self.step + self.distance_to_ride_start(ride) + self.wait_time(ride) + ride.distance()

    def can_start_on_time(self, ride):
        return self.step + self.distance_to_ride_start(ride) <= ride.step_min

    def can_finish_in_time(self, ride, steps):
        can_finish = self.arrival(ride) <= min(ride.step_max, steps)
        return can_finish

    def assign(self, ride):
        self.assigned_rides.append(ride.rid)
        step_departure = max(ride.step_min, self.step + self.distance_to_ride_start(ride))
        self.step = step_departure + ride.distance()
        self.x = ride.x2
        self.y = ride.y2


def check_vehicles(expected, value):
    """
    Check number of vehicles found in output file matches input specifications
    :param expected: number of cars as specified by input file
    :param value: number of cars found in output file
    :return: value == expected
    """
    logging.info("checking vehicles")
    if value != expected:
        logging.warning("found {} cars in output file, expected {}".format(value, expected))
    return value == expected


def check_ride_ids(vehicles_rides, rides):
    """
    Check ride ids are assigned at most once
    :param vehicles_rides: vr[i] == ride list of vehicle i
    :param rides: number of rides as specified by input file
    :return: True if ride ids assigned at most once else False
    """
    rids_assigned = set()
    assigned_at_most_once = True
    valid_range = True
    logging.info("checking ride ids")
    for vehicle, rids in enumerate(vehicles_rides):
        for rid in rids:
            if rid < 0 or rid >= rides:
                logging.warning("line {}: invalid rid {} < 0 or >= {}".format(vehicle, rid, rides))
                valid_range = False
            if rid in rids_assigned:
                logging.warning("rid {} was assigned more than once".format(rid))
                assigned_at_most_once = False
            else:
                rids_assigned.add(rid)
    return assigned_at_most_once and valid_range


def parse_input(file_in):
    """
    Parse input file
    :param file_in: input file name
    :return: rides_list, rows, columns, vehicles, rides, bonus, steps
    """
    logging.debug("parsing {}".format(file_in))
    with open(file_in, 'r') as f:
        first_line = f.readline()
        rows, columns, vehicles, rides, bonus, steps = tuple([int(x) for x in first_line.split(' ')])
        logging.debug("{} {} {} {} {} {}".format(rows, columns, vehicles, rides, bonus, steps))
        rides_list = []
        for rid, line in enumerate(f.readlines()):
            ride = tuple([int(x) for x in line.split(' ')])  # x1, y1, x2, y2, step_start, step_end
            rides_list.append(Ride(rid, *ride))
    logging.debug("parsing {}: done".format(file_in))
    return rides_list, rows, columns, vehicles, rides, bonus, steps


def parse_output(file_out):
    """
    Return ride list parsed from output file
    :param file_out: output file name (solution)
    :return: vehicle rides, vr[i] == ride list of vehicle i
    """
    logging.debug("parsing {}".format(file_out))
    vehicles_rides = []
    with open(file_out, 'r') as f:
        for line in f.readlines():
            rides = list(map(int, line.split(' ')))
            vehicles_rides.append(rides[1:])  # rides[0] == number of rides
    logging.debug("parsing {}: done".format(file_out))
    return vehicles_rides


def eval_ride(car, ride, score, bonus, steps):
    """
    Modified return values, so that returned integer
    corresponds to json indicator,
    see https://github.com/sbrodehl/Hashcode2k18/issues/2.

    :param car: assigned
    :param ride: to evaluate
    :param bonus: bonus points as specified by input file
    :param steps: simulation duration as specified by input file
    :return: ride completed in time
    """
    score.taken += 1
    if car.can_finish_in_time(ride, steps):
        if car.can_start_on_time(ride):
            score.bonus_score += bonus  # bonus points
            score.wait_time += car.wait_time(ride)
            score.bonus += 1  # departures on time
            score.raw_score += ride.distance()
            car.assign(ride)
            return 1000
        score.raw_score += ride.distance()
        car.assign(ride)
        return 1
    else:  # late
        car.step = car.arrival(ride)
        car.x = ride.x2
        car.y = ride.y2
        score.late += 1
        return 0


def compute_score(file_in, file_out, check=False):
    """
    Compute score (with bonus) of submission
    :param file_in: input file
    :param file_out: output file (solution)
    :param check: if True checks cars number and ride ids uniqueness (slower)
    :return: score, input data
    """
    (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(file_in)
    vehicles_rides = parse_output(file_out)
    if check:
        if check_vehicles(vehicles, len(vehicles_rides)):
            logging.info("vehicles: OK")
        if check_ride_ids(vehicles_rides, rides):
            logging.info("ride ids: OK")
    score = Score()
    for vehicle_rides in vehicles_rides:
        car = Car()
        for rid in vehicle_rides:
            ride = rides_list[rid]
            eval_ride(car, ride, score, bonus, steps)
    score.unassigned = rides - score.taken
    return score


def set_log_level(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description='print score',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_in', type=str, help='input file e.g. a_example.in')
    parser.add_argument('file_out', type=str, help='output file e.g. a_example.out')
    parser.add_argument('--debug', action='store_true', help='for debug purpose')
    parser.add_argument('--score', action='store_true', help='display raw score and bonus score')
    parser.add_argument('--wait', action='store_true', help='display wait time')
    parser.add_argument('--rides', action='store_true', help='display rides stats')
    parser.add_argument('--check', action='store_true', help='check output (slower)')
    args = parser.parse_args()
    set_log_level(args)
    score = compute_score(args.file_in, args.file_out, args.check)
    if args.score:
        print("score: {0:,} = {1:,} + {2:,} (bonus)".format(score.total(), score.raw_score,
                                                            score.bonus_score))  # decimal separator
    else:
        print("score: {0:,}".format(score.total()))  # decimal separator
    if args.wait:
        print("wait time: {0:,}".format(score.wait_time))  # decimal separator
    if args.rides:
        print("rides: {0:,} = {1:,} (taken) + {2:,} (unassigned) {3:,} (late)".format(score.taken + score.unassigned,
                                                                                      score.taken, score.unassigned,
                                                                                      score.late))  # decimal separator
        print("rides: {0:,} (taken) = {1:,} (bonus) + {2:,} (no bonus)".format(score.taken, score.bonus,
                                                                               score.taken - score.bonus))  # decimal separator


if __name__ == '__main__':
    main()
