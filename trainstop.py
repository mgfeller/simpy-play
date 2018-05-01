# -*- coding: utf-8 -*-
from train import Train


class TrainStop:

    def __init__(self, name, env):
        self.env = env
        self.name = name

    def train_arrived(self):
        yield self.env.timeout(1)
        return Train(["C", "D"])
