from enum import unique, Enum


@unique
class CourseSearchType(Enum):
    """
    Class for enumerating course languages
    """

    COURSEID = 1
    COURSENAME = 2

