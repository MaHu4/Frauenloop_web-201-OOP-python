from models.teacher import SchoolTeacher #from folder_name.file_name import class

# PhysicsTeacher = child class of SchoolTeacher (Inheritance)
# ?? super is an object and not a class name to access parameters and methods of a parent class from inside a child class, herer SchoolTeacher
# ?? Why name = name and not only name??

class PhysicsTeacher(SchoolTeacher): 
    def __init__(self, name, lab_number):  ## ??? parameterized constructor; default constructor without lab_number. Are other methods aso caled cosntructors or ony init-method
     
        super().__init__(name=name)  
        self.lab_number = lab_number # ??? is this an object???

    def get_lab_number(self):
        return self.lab_number # lab number is defined in main_controller.py