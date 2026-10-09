"""
In a future where robots are as common as smartphones, you are hosting a Robot Dance Party and need a simple system to manage your robot dancers.

You will design two classes that work together to simulate the event:

Class RobotDancer: represents a single robot dancer.
Each robot should have:
robot_id: a unique identifier for the robot.
name: the robot's name.
dance_move: the name of its dance move (e.g., "Moonwalk", "Robot Wave").The class should include a method dance() that prints a message like:
R2D2 is doing the Moonwalk!
Class DanceFloor: represents the dance floor where robots perform.
It should:
Store a list of RobotDancer objects.
Include a method add_robot(robot) to add a new robot to the floor.
Include a method display_robots() that lists the name of the robots currently on the dance floor. Print a special message in case there are no robots on the dance floor.
Include a method start_dancing() that makes all robots perform their dance moves by calling each robot's dance() method. 
Print a special message in case there are no robots on the dance floor.
Check the example code to see how to implement and use the classes correctly.

"""

# Example usage



class RobotDancer:


    def __init__(self, robot_id, name, dance_move):
        self.robot_id = robot_id
        self.name = name
        self.dance_move = dance_move
    

    def dance(self):
        print(f"{self.name} is doing the {self.dance_move}!")


    def __str__(self):
        return f"{self.robot_id} {self.name} {self.dance_move}"




class DanceFloor:

    def __init__(self):
        self.robot_dance = []

    
    def add_robot(self, robot):
        self.robot_dance.append(robot)
    

    def display_robots(self):
        pass

    
    def start_dancing(self):
        pass


    def __str__(self):
        return f"{self.robot_dance}"






# This should consider that there are no robots on the dance floor
dance_floor = DanceFloor()
dance_floor.display_robots()
dance_floor.start_dancing()

# Robot Dancers
r2d2 = RobotDancer(1, "R2D2", "Moonwalk")
wall_e = RobotDancer(2, "Wall-E", "Robot Wave")
bender = RobotDancer(3, "Bender", "Circuit Salsa")

# Dance Floor Setup
# dance_floor.add_robot(r2d2)
# dance_floor.add_robot(wall_e)
# dance_floor.add_robot(bender)

# Party Time!
# dance_floor.display_robots()
# dance_floor.start_dancing()