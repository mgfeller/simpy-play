class Passenger:

    def __init__(self, name, env, journey):
        self.name = name
        self.env = env
        self.journey = journey
        self.status = 'waiting'

    def wait_for_train(self, train_stop):
        while self.status == 'waiting':
            train = yield self.env.process(train_stop.train_arrived())
            if train.stops_at(self.journey.to_stop):
                self.status = 'traveling'
                print("passenger %d traveling on train %s" % (self.name, train))
