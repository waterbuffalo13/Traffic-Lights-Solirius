from itertools import cycle, islice
from Lights import TrafficLight
import threading
import pandas as pd
from datetime import datetime


class GenerateTraffic:
    def __init__(self, number):
        self.number = number
        self.counter = 1
        self.isOne = False

        self.colours_list = ["Red Light", "Green Light", "White Light"]
        col_length = len(self.colours_list)
        self.colours_modified = []
        for x in range(0, self.number):
            self.colours_modified.append(self.colours_list[x % col_length])

        # self.colours_modified = list(islice(cycle(self.colours_list), number))

        self.traffic_whole = []
        for i, x in zip(range(number), self.colours_modified):
            self.traffic_whole.append(TrafficLight(x, "off", i + 1))

    def runProgram(self):
        threading.Timer(1.0, self.runProgram).start()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        # loop through traffic lights
        for light in self.traffic_whole:
            if self.number == 1:
                if not self.isOne:
                    light.state = "on"
                    self.isOne = True
                elif self.isOne:
                    light.state == "off"
                    self.isOne = False






            else:
                # if light matches counter, turn on and print
                if light.position == self.counter:
                    light.state = "on"
                    # print(current_time + " " + str(light))
                # turn previous light off
                if light.position == self.counter - 1:
                    light.state = "off"
                    # print(current_time + " " + str(light))

        print(current_time + " " + str(self.traffic_whole) + " counter:" + str(self.counter))
        if self.counter == self.number:
            # print(current_time + " " + str(light))
            light.state = "off"
            self.counter = 1

        else:
            self.counter = self.counter + 1
