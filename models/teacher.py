import string   # ??? where is string imported from?? What is this?

class SchoolTeacher:

# parameterized Constructor - a special function linked to a class
    def __init__(self, name):  #function = __init__ makes SchoolTeacher an object, self = keyword of class, name = variable as placeholder for data
        self.name = name

    def get_name(self) -> string:
        return self.name