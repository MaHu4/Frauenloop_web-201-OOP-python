from models.teacher import SchoolTeacher

class MathsTeacher(SchoolTeacher): 
    def __init__(self, name, form_teacher, room_number_main_form, other_forms, room_number_other_forms): 
                                        # form_teacher and room_number_main_form added (in comparison to physics teacher); form (Brit) for Schulklasse
        super().__init__(name = name)
                        # ??? WHY name = name and not just name??; ony =, not == because it's a function; it's supposed to do something
        self.form_teacher = form_teacher
        self.room_number_main_form = room_number_main_form 
        self.other_forms = other_forms
        self.room_number_other_forms = room_number_other_forms
