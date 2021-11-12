raka = ["Raka Ardhi",28, "CurDev", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard Mccoy", "Chief Medical Officer", 2266]

class Dog():
    species = "Canis familiaris"
    
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
miles= Dog('Miles',6)
print(miles.age)
print(miles.name)
print(miles.description())
print(miles.speak("woof"))
    
class Mom():
    def __init__(self,name, hair_color):
        self.name = name
        self.hair_color = hair_color

class Children(Mom):
    def __init__(self, name, new_hair_color):
        self.hair_color = new_hair_color
        self.name = name
        
mom = Mom('ani', 'coklat')
print(f"{mom.name}'s hair color is {mom.hair_color}")
first_daughter = Children('ita','ungu')
print(f"{first_daughter.name}'s hair color is {first_daughter.hair_color}")

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

buddy = JackRussellTerrier("Buddy", 2)

print(buddy.speak())