class Mother:
    mothername = "SITA"
    def mother(self):
        print(self.mothername)
class Father:
    fathername = "RAM"
    def father(self):
        print(self.fathername)
class Son(Mother, Father): # Son inherits from BOTH Mother and Father
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.parents() # Has access to attributes from both parent classes
