class Parent:
    parentAttr = 100
    def parentMethod(self):
        print("Calling parent method")
class Child(Parent): # Child inherits from Parent
    def childMethod(self):
        print("Calling child method")
c = Child()          # Create instance of child
c.childMethod()      # Child calls its own method
c.parentMethod()     # Child successfully calls inherited parent's method
print(c.parentAttr)  # Child accesses inherited parent attribute (100)
