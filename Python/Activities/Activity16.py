#with open("sample.csv", "r") as file:
 # for line in file:
 #   print(line)

#class MyClass:
#  'This is an example class'
#  x = 5
  
#p1 = MyClass()
#print(p1.x) # Output: 5   

#print(MyClass().x)

#class person:
#    def __init__(self, name, age):
#        self.name= name
#        self.age = age

#p1= person("john", 6)   

#print(p1.name, p1.age)
###################Activity 16##########
#----------------Create a car class with the following details:
# #Properties: manufacturer, model, make, transmission, color
# Methods: accelerate(), stop()
# accelerate() should print "{Manufacturer} {Model} is moving"
# stop() should print "{Manufacturer} {Model} has stopped"

class Car:
    def __init__(self, manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model=model
        self.make =make
        self.transmission= transmission
        self.color = color
    def accelerate(self):
        print(self.manufacturer + " " + self.model + " is moving")
    def stop(self):
        print(self.manufacturer + " " + self.model + " has stopped")

car1 = Car("Toyota", "Corolla", "2015", "Manual", "White")
car2 = Car("Maruti", "800", "2013", "Manual", "Red")
car3 = Car("Suzuki", "Swift", "2017", "Automatic", "Black")
car1.accelerate()
car1.stop()