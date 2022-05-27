class Course:

    def __init__(self, course_id: int, course_name: str):
        self.__course_id: int = course_id
        self.__course_name: str = course_name


    def __str__(self):
        return f"Course ID: {str(self.__course_id)}, Course name: {str(self.__course_name)}," \
               f" Course responsible: {str(self.__course_responsible)}, Course Location:  "

    def get_course_id(self):
        return self.__course_id

    def set_course_responsible(self, new_course_responsible: str):
        self.__course_responsible = new_course_responsible

    def get_course_responsible(self):
        return self.__course_responsible

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, new_course_id: int):
        self.__course_id = new_course_id

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, new_course_name: str):
        self.__course_name = new_course_name
