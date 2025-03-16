class Student:
    def __init__(self,student_id,name,age):
        self.student_id=student_id
        self.name=name
        self.age=age
    
    def display_info(self):
        print("ID: %d번 / 이름 : %s / 나이: %d살"%(self.student_id,self.name,self.age))


class StudentManager:
    def __init__(self):
        self.students=[]




    def add__student(self,student):
        self.students.append(student)



    def display_all_students(self):
        for i in self.students:
            print("ID: %d번 / 이름 : %s / 나이: %d살"%(i.student_id,i.name,i.age))

student1=Student(1,"김철수",20)           
student2=Student(2,"이영희",21)           
student3=Student(3,"박지민",19) 
print("현재 등록된 학생 목록")
student1.display_info()          
student2.display_info()          
student3.display_info()          
manager=StudentManager()
manager.add__student(student1)
manager.add__student(student2)
manager.add__student(student3)
student4=Student(4,"한지수",22)
manager.add__student(student4)
print("\n학번 4번 학생 추가 후")
manager.display_all_students()
