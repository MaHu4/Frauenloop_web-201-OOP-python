from views.school_students import SchoolStudents
from models.student import Student
 
class TestSchoolStudents:
 
    # TODO Task1.0: write test

    def test_enroll_student(self):

        schoolStudents = SchoolStudents()
        print(type(schoolStudents))

        #  variable of type Student
        firstStudentInClass = Student(name="Maria", age=20, class_number=5)

        # METHOD TO TEST: enroll your first student
        schoolStudents.enroll_student(firstStudentInClass)

        assert schoolStudents.enrolled_students == [firstStudentInClass]
    
    # TODO Task1.1: write test
    def test_fetch_all_student_data(self):  

        # test-setup
        schoolStudents = SchoolStudents() # new object of SchoolStudents (not same object as in Task1.0)
        #variable of type student
        firstStudentInClass = Student(name="Maria", age=20, class_number=5)
        secondStudentInClass = Student(name="Jyotsna", age=20, class_number=5)

        #enroll a student
        schoolStudents.enroll_student(firstStudentInClass)
        schoolStudents.enroll_student(secondStudentInClass)

        # method to test
        all_student_data = schoolStudents.fetch_all_student_data()

        # assertion of actual result == expected result 
        assert all_student_data == [firstStudentInClass, secondStudentInClass]


    # TODO Task1.2: write test for fetch_data_with_student_name()