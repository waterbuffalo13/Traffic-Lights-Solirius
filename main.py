from GenerateTrafficLights import GenerateTraffic

if __name__ == '__main__':
    try:
        x = int(input("How many traffic lights do you want to generate? (default = 20)"))
        GenerateTraffic(x).runProgram()
    except ValueError:
        print("Oops!  That was not a valid number.  Let's try with twenty")
        x = 20
        GenerateTraffic(x).runProgram()


