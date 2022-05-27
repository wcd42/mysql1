from Course import Course
from ActiveSystem import ActiveSystem
from mysql1.DAO_MySQL import DAO_MySQL

# This is the main file that launches the application
# A couple of employees are created and manipulated before the GUI is started


def main():

    course1 = Course(1, "systemdev")

    # create a DAO (database access object)
    courseDAO = DAO_MySQL()

    ActiveSystem.set_dao(courseDAO)
    # set up the database (drop the existing table!)
    courseDAO.setup()
    # start a connection to the database
    # connect to the database
    courseDAO.connect()

    courseDAO.insert_course(course1)



