class Student:
    def __init__(self, Name, Rollno):
        self.name = Name
        self.rollno = Rollno
        
    def showDetail(self):
        print(f"Roll No.:{self.rollno}")
        print(f"Name of Student.:{self.name}")

class Marks:
    def __init__(self, Math, Science, English):
        self.math = Math
        self.science = Science
        self.english = English
        
    def showMark(self):
        print(f"Math mark:{self.math}")
        print(f"Science mark:{self.science}")
        print(f"English mark:{self.english}")
        
    def totalMarks(self):
        return self.math + self.science + self.english
    
class Result(Student, Marks):
    def __init__(self, Name, Rollno, Math, Science, English):
        Student.__init__(self, Name, Rollno)
        Marks.__init__(self, Math, Science, English)
        
    def percentage(self):
        result = self.totalMarks()/3
        print(f"Result:{round(result,2)}%")
        
    def showResult(self):
        self.showDetail()
        self.showMark()
        print(f"Total marks obtained:{self.totalMarks()} outof 300")
        self.percentage()
        
student = Result("Rahul",21,98,79,81)
student.showResult()