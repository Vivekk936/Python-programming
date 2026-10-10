#method overriding
class Grandparent:
    def speak(self):
        print("HEllo my name is amit")
class Parent(Grandparent):
    def speak(self):
        print("Hello my name is Junioir amit")
class Child(Grandparent):
    def speak(self):
        print("Hello my name is junior amit junior")

def attribute_provider(objects):
    print(objects.speak())


obj= Grandparent()
attribute_provider(obj)
parent=Parent()
attribute_provider(parent)
cchild=Child()
attribute_provider(cchild)

                        