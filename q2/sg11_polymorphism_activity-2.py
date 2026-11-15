"""

Answer the following questions:
    a. What is duck typing, as explained in the video?
        - It is a alternate way to achieve polymorpism instead of using inheritance. It follows the statement/analogy: "If it looks like duck and quacks like a duck, it must be a duck."

    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
        - The Car class needs to have the same speak() method in order to work inside the same loop as Dog and Cat.
        
"""

class Caar():
  def move(self):
    print("The car drives on the road.")

class Boat(): 
  def move(self):
    print("The boat sails on water.")

class Drone():
  def move(self):
    print("The drone flies in the sky.")

vehicle = [Car(), Boat(), Drone()]

def start_trip(vehicle):
  for i in vehicle:
      i.move()

start_trip(vehicle)


