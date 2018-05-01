# -*- coding: utf-8 -*-

import simpy
import random

from journey import Journey
from passenger import Passenger
from trainstop import TrainStop

random.seed(42)
destinations = ["B", "C", "D"]


class PassengerScheduler:

    def __init__(self, env, train_stop):
        self.env = env
        self.env.process(self.schedule())
        self.train_stop = train_stop

    def schedule(self):
        count = 0
        while True:
            count += 1
            destination = random.choice(destinations)
            trip = Journey("A", destination)
            passenger = Passenger(count, self.env, trip)
            print("Sending passenger %d on the trip %s at %d" % (count, trip, self.env.now))
            self.env.process(passenger.wait_for_train(self.train_stop))
            yield self.env.timeout(5)


def main():
    env = simpy.Environment()
    PassengerScheduler(env, TrainStop("A", env))
    env.run(until=30)


if __name__ == "__main__":
    main()
