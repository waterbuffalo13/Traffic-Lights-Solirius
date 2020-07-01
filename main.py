from Lights import TrafficLight
from itertools import cycle, islice
from GenerateTraffic import GenerateTraffic

def generateTrafficLights(count):
    traffic_whole = []
    colours = ["red","green","white"]
    colours_gen = list(islice(cycle(colours),count))

    for i,x in zip(range(count), colours_gen):
        traffic_whole.append(TrafficLight(x,"off", i+1))
    print(traffic_whole)

if __name__ == '__main__':
     GenerateTraffic(20)

