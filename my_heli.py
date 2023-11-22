from ubicoders_vrobots import System, Helicopter

# Create a helicopter object that contains states (position and velocity)
heli = Helicopter()

class UbicodersMain:
    def __init__(self) -> None:
        # Define the variables here!
        pass
    
    def setup(self):
        # This API will be released soon!
        # heli.mass = 2 #kg
        pass

    def loop(self):
        # Print the helicopter states from the simulator!
        states = heli.states
        print(states)

        # Set the thrust force to the helicopter!
        heli.set_force(16) # Newton

if __name__ == "__main__":
    sys = System(heli, UbicodersMain())
    sys.start()
