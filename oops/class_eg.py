class students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def get_grade(self):
        return self.grade
    

class course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def average_grade(self):
        val=0
        for student in self.students:
            val += student.get_grade()
        return val/len(self.students)
    

s1=students('Bill',19,90)
s2=students('Till',19,95)
s3=students('Tim',19,80)

course=course('Science',2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.students)
print(course.average_grade())