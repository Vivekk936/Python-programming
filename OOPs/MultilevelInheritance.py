class Grandfather:
    def __init__(self,nationality,anger_issue):
        self.nationality=nationality
        self.anger_issue=anger_issue

    def introduction(self):
        print("Nationality:"+self.nationality)
        print("Anger Issue:"+self.anger_issue)
class Parent(Grandfather):
    def __init__(self,nationality,anger_issue,intelligence):
        super().__init__(nationality,anger_issue)
        self.intelligence=intelligence            

    def intro(self):
        print("Inteligence",self.intelligence)    
class Child(Parent):
    def __init__(self,nationality,anger_issue,intelligence,iq):
        super().__init__(nationality,anger_issue,intelligence)
        self.iq=iq
    def iq1(self):
        print("IQ is good of child:",self.iq)

parent_1=Parent("Indian","Less Anger Issue","Good intelligence")
parent_1.intro()
parent_1.introduction()
child=Child("Indian","Less Anger issue","Good intelligence","High")
child.introduction()
child.intro()
child.iq1()

