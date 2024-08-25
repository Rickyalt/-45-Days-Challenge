class Student:

    def __init__(self, name):
        self.name= name
        self.grades= []

    def add_grade(self, grade):
        if 0<=grade<= 100:
            self.grades.append(grade)
            return sum(self.grades)
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")   

    def sum_of_grades(self):
        return sum(self.grades)         

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)        
    
    def display(self):
        average = self.calculate_average()
        summ=self.sum_of_grades()
        print("Student:",self.name)
        print("Grades:",self.grades)
        print("The sum of the grades is:",summ)
        print("Average Grade:",average)


student = Student(input("Enter the name of the student:"))
n=int(input("Enter the number of grades:"))
for i in range(n):
    grade=int(input("Enter the grade:"))
    student.add_grade(grade)

student.display()