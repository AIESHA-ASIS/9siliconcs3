class Animal():
  def __init__(self,name):
    self.name = name

  def eat(self):
    return f"{self.name} eats food."

  def make_sound(self):
    return f"{self.name} makes a sound."

class Lion(Animal):
  def eat(self):
    return f"{self.name} eats fresh meat!"

  def make_sound(self): 
    return f"{self.name} roars loudly!"

class Elephant(Animal):
  def eat(self):
    return f"{self.name} eats Grass and fruit."

  def make_sound(self):
    return f"{self.name} trumpets!"

class Monkey(Animal):
  def eat(self):
    return f"{self.name} eats bananas."

  def make_sound(self):
    return f"{self.name} chatters! "

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")

    
  