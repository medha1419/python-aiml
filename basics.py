print("\n9. OOP")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

    def passed(self):
        return self.marks >= 40

s1 = Student("Medha", 85)
s2 = Student("Aman", 32)

s1.display()              # Medha 85
print(s1.passed())        # True

s2.display()              # Aman 32
print(s2.passed())        # False