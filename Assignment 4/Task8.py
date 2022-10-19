
# Write your code here.
class Student():
    def __init__(self,name,id,dept = "CSE"):
        self.name = name
        self.id = id
        self.dept = dept
        self.time = 0

    def dailyEffort(self,time):
        self.time = time

    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}\nDaily Effort: {self.time} hour(s)")
        if self.time<= 2:
            print( 'Suggestion: Should give more effort!')
        elif self.time<= 4:
            print( 'Suggestion: Should give more effort!')
        else:
            print( 'Suggestion: Excellent! Now motivate others.')


harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()