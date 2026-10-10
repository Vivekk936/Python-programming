class Avenger:
    def __init__(self,name,strength):
        self.name=name
        self.strength=strength
    def __add__(self,other):
        return Avenger(self.name+"&"+other.name,self.strength+other.strength)
    def __str__(self):
        return f"{self.name} with combined strength {self.strength}"

ironman=Avenger("IronMan",90)
thor=Avenger("Thor",100)
team=ironman+thor
print(team)    