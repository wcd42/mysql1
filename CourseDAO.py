from abc import abstractmethod
from mysql1.DAO import DAO
from mysql1.Course import Course
from typing import List
from mysql1.CourseSearchType import CourseSearchType


class CourseDAO(DAO):

    @abstractmethod
    def insert_course(self, course: Course):
        pass

    @abstractmethod
    def update_course(self, course: Course) -> bool:
        pass

    @abstractmethod
    def delete_course(self, course: Course) -> bool:
        pass

    @abstractmethod
    def find_course_by_property(self, search_type: CourseSearchType, value: object) -> List[Course]:
        pass

    @abstractmethod
    def find_all(self) -> List[Course]:
        pass