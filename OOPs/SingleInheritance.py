class Avenger:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def intro(self):
        print(f"Hello i am {self.name} my power is {self.power}") 
class IronMan(Avenger):  
    def __init__(self, name, power,weapon):

        super().__init__(name, power)
        
        self.weapon=weapon
    def weapon_details(self):
        print(f"I use {self.weapon}") 

iron=IronMan("Ironman","Jarvis","Ironman suit")
iron.intro()
iron.weapon_details()