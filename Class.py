class Car:
    manufacturer = "temp"
    def __init__(self, chassi_number):
        self.chassi_number = chassi_number
        self.model = "temp"
    
car1 = Car("11-A5")
print(car1.chassi_number)

car1.manufacturer = "toyota"
print(car1.manufacturer)

class Person:
    def __init__(self, title="default_title"):
        self._name = None
        self.title = title
    def talk(self):
        print("I'm a person")
    def talk(self):
        print("I'm Walking")

class SportsPerson(Person):
    def __init__(self, id, title):
        super().__init__(title)
        self.id = id

    def talk(self):
        print("I'm a sportsperson")

person3 = SportsPerson(2, "p3")

def check_talk(obj):
    obj.talk()

check_talk(person3)
person3.talk()



