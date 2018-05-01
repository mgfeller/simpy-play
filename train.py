# -*- coding: utf-8 -*-


class Train:

    def __init__(self, stops):
        self.stops = stops

    def __str__(self):
        return "<Train to %s>" % ", ".join(self.stops)

    def stops_at(self, where):
        return where in self.stops
