# class Dog:
#     specie = "canifarous teterous"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"

#     @classmethod
#     def info(cls):
#         return f"I am of {cls.specie}"


# print(Dog.info())

# dog1 = Dog(name = "cucudio", age = "32")  #instance attribute cause it varies from one object to another
# dog2 = Dog(name = "neff", age = "23")
# print(dog1 == dog2)

# dog1 = Dog("cucudio", 32) 
# dog2 = Dog("neff", 23)

# disc = dog1.description()
# sp = dog1.speak("Woof woof")

# print(Dog.info())

# print(dog1.name)
# print(dog2.name)
# print(dog1.specie)
# print(dog2.specie)

# Dog.specie = "omnivorous cucudio"
# print(dog1.specie)
# print(dog2.specie)
# print(Dog.specie)

# instance method are functions that are defined inside a class and can only be called from an instance of that class' 

# def description(self):
#     return f"{self.name} is {self.age} years old"

# def speak(self, sound):
#     return f"{self.name} says {sound}"

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def input_sides(self):
#         self.sides = [float(input("Enter side" + str(i + 1) + " : ")) for i in range(self.n)]  

#     def dispsides(self):
#         for i in range(self.n):
#             print("side", i+1, "is", self.sides[i])    

a = 2 + 6
print(a)
