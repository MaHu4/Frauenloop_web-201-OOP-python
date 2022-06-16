from models.student import Student

class TestStudent:
    def test_calculate_dob(self):
        st = Student(name="Test name", age=29, class_number=2)
        assert st.calculate_dob(2022) == 1992
