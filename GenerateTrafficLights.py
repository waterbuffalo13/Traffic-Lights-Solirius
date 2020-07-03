from itertools import cycle, islice
from Lights import TrafficLight
import threading
import pandas as pd
from datetime import datetime, timedelta
import time


class GenerateTraffic:
    def __init__(self, number):
        self.number = number
        self.counter = 0
        self.isOne = False

        self.colours_list = ["Red Light", "Green Light", "White Light"]
        col_length = len(self.colours_list)

        self.colours_modified = []
        for x in range(0, self.number):
            self.colours_modified.append(self.colours_list[x % col_length])

        # self.colours_modified = list(islice(cycle(self.colours_list), number))

        self.traffic_whole = []
        for i, x in zip(range(number), self.colours_modified):
            self.traffic_whole.append(TrafficLight(x, "off", i))

    def runProgram(self):
        # threading.Timer(1.0, self.runProgram).start()
        while(True):
            if self.number == 1:
                print("rip")
            else:
                index = 0
                light = self.traffic_whole
                current_time = datetime.now().strftime("%H:%M:%S")
                while index < len(light):
                    if light[index].position == self.counter:
                        time.sleep(1)
                        light[index].state = "on"

                        print(current_time + " " + str(light[index]))

                    #turn of behind initial variable from 0-len(9)
                    elif light[index].position == self.counter - 1:# and (self.counter-1) >= 0 and self.counter < self.number:
                        light[index].state = "off"

                        print(current_time + " " + str(light[index]))

                    #reach end of loop
                    elif self.counter == self.number:
                        light[self.counter - 1].state = "off"
                        self.counter = 0
                        index = -1

                        print(current_time + " " + str(light[index]))
                    else:
                        pass
                    index += 1
                self.counter += 1

