from mysql1.CourseDAO import CourseDAO
from mysql1.Course import Course
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from mysql1.CourseSearchType import CourseSearchType
from typing import List

class DAO_MySQL(CourseDAO):
    DB_NAME = 'KUDB'

    __pool__: pooling.MySQLConnectionPool
    __cnx__: mysql.connector.connection = None
    cursor = None

    @classmethod
    def create_database(cls):

        cls.__cnx__ = mysql.connector.connect( user='root',
                                               password='Halo4242',
                                               host='127.0.0.1')
        cursor = cls.__cnx__.cursor()
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(cls.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    @classmethod
    def setup(cls):
            cls.__cnx__ = mysql.connector.connect(user='root',
                                                  password='Halo4242',
                                                  host='127.0.0.1')

            cursor = cls.__cnx__.cursor()
            try:
                cursor.execute("USE {}".format(cls.DB_NAME))
            except mysql.connector.Error as err:
                print("Database {} does not exists.".format(cls.DB_NAME))
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    cls.create_database()
                    print("Database {} created successfully.".format(cls.DB_NAME))
                    cls.__cnx__.database = cls.DB_NAME
                else:
                    print(err)
                    exit(1)

            create = """
            DROP TABLE IF EXISTS `Courses`;
            CREATE TABLE `Courses` (
                `idCourse` int NOT NULL,
                `course_name` varchar(45) NOT NULL,
                PRIMARY KEY (`idCourse`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
            """
            with cls.__cnx__.cursor() as cursor:
                cursor.execute(create)

    @classmethod
    def connect(cls):
        try:
            cls.__pool__ = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, user='root',
                                                        password='Halo4242',
                                                        host='127.0.0.1', database=cls.DB_NAME)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cls.__cnx__.close()

            cls.__cnx__ = cls.__pool__.get_connection()
            print("connection", cls.__cnx__)

    def close(cls):
        if cls.__cnx__ is not None:
            cls.__cnx__.close()

    @classmethod
    def insert_course(cls, course: Course):
        idCourse = course.get_course_id()
        course_name = course.get_course_name()

        insert = """
                    INSERT into KUDB.Courses (idCourse, course_name)  
                    VALUES ("%s", "%s") 
                    """ % (idCourse, course_name)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(insert)
            cls.__cnx__.commit()

    @classmethod
    def update_course(cls, course: Course) -> bool:
        idCourse = course.get_course_id()
        course_name = course.get_course_name()

        update = """
            UPDATE KUDB.Courses 
            SET idCourse = "%s", course_name = "%s" 
            """ % (idCourse, course_name)

        cls.__cnx__ = mysql.connector.connect(pool_name="mypool")

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(update)
            cls.__cnx__.commit()

    @classmethod
    def delete_employee(cls, course: Course):
        idcourse = course.get_course_id()

        delete = """
                DELETE FROM KUDB.Courses 
                WHERE idCourse="%s"
                """ % idcourse

        cls.__cnx__ = mysql.connector.connect(pool_name="mypool")

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(delete)
            cls.__cnx__.commit()

    def find_course_by_property(self, search_type: CourseSearchType, value: object) -> List[Course]:
        pass

    @classmethod
    def find_all(cls) -> List[Course]:

        query = "SELECT * FROM KUDB.Courses"
        print("findall connection", cls.__cnx__)
        cursor = cls.__cnx__.cursor(dictionary=True)
        with cls.__cnx__.cursor(dictionary = True) as cursor:
            cursor.execute(query)
        all_courses = cursor.fetchall()
        print(all_courses)
        print(cls.__pool__)
        return all_courses