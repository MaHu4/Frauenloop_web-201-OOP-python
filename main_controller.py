from models.student import Student
from models import physics_teacher
from views.school_students import SchoolStudents
from models.subject import SchoolSubject
from models.maths_teacher import MathsTeacher # added

student1 = Student(name="Jyotsna", age="29", class_number="3") # turned age and class_number from int to string by adding  
# Student = data type (can't be printed), student1 = Object
# access class variables
print("Student details:") # added this line
print("Name: " + student1.name) # added string in beginning
print("Age: " + student1.age)  # added string in beginning
print("Class: " + student1.class_number)  # added string in beginning

student2 = Student(name="Angela", age="28", class_number="4") # added line; data from line 7 are replaced in terminal through new line
print("Student details:") # added this line
print("Name: " + student2.name) # added string in beginning
print("Age: " + student2.age)  # added string in beginning
print("Class: " + student2.class_number)  # added string in beginning


# SchoolStudents().enroll_student(student) # Question: why is this line printed in the terminal??
SchoolStudents().all_students()

# TODO: put into a view
# enroll_teachers()

# PHYSICS TEACHER

## ??? HOW can we link teacher to students?? Define them as parameter in ()?? Would that be poymorphism
physics_teacher_1 = physics_teacher.PhysicsTeacher(name="Mia", lab_number="101") # object1 # ??? Only strings possible??
physics_teacher_2 = physics_teacher.PhysicsTeacher(name="Hubert", lab_number="102") #object2


print("Physics teacher details:")
print("Name: " + physics_teacher_1.name, ", Lab number: " + physics_teacher_1.get_lab_number()) #?? Why get_let_number??; only .lab_number works as well 
print("Name: " + physics_teacher_2.name, ", Lab number: " + physics_teacher_2.lab_number)

# MATH TEACHERS (added)
# ??? why maths_teacher not defines????

maths_teacher_1 = maths_teacher.MathsTeacher(name="Mia", form_teacher="5.b", room_number_main_form = "304", other_forms = "7.a, 6.b", room_number_other_forms = "406, 507") # object1
maths_teacher_2 = maths_teacher.MathsTeacher(name="Hubert", form_teacher="6.c", room_number_main_form = "204", other_forms = "7.a, 6.b", room_number_other_forms = "405, 305") #object2

print("Maths teacher details:")
print("Name: " + maths_teacher_1.name, ", Form Teacher of: " + maths_teacher_1.form_teacher, "Room Number of main form: " + maths_teacher_1.room_number_main_formn, "Other forms: " + maths_teacher_1.other_forms, "Room Numbers of other form: " + maths_teacher_1.room_number_other_forms) 
print("Name: " + maths_teacher_2.name, ", Form Teacher of: " + maths_teacher_2.form_teacher, "Room Number of main form: " + maths_teacher_2.room_number_main_formn, "Other forms: " + maths_teacher_2.other_forms, "Room Numbers of other form: " + maths_teacher_2.room_number_other_forms) 


# create a new object of type SchoolSubject and print its name

school_subject = SchoolSubject(name="Physics")
print("School Subject details:") # added this line
print(school_subject.name)