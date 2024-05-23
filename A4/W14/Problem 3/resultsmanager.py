import os
import sys
import sqlite3

from result import Result
from student import Student
from course import Course


class ResultsManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(
            sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()

    def create_tables(self):
        self.dbc.execute('''CREATE TABLE IF NOT EXISTS courses
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          points INTEGER NOT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS students
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT NOT NULL,
                          last_name TEXT NOT NULL,
                          date_of_birth DATE NOT NULL,
                          class_code TEXT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS results
                         (student_id INTEGER NOT NULL,
                          course_id INTEGER NOT NULL,
                          mark INTEGER NOT NULL,
                          achieved DATE NOT NULL,
                          PRIMARY KEY(student_id, course_id, mark));''')

        self.conn.commit()

    def get_course(self, course_id) -> Course:
        raise NotImplementedError

    def add_course(self, course: Course) -> Course:
        raise NotImplementedError

    def get_student(self, student_id) -> Student:
        raise NotImplementedError

    def add_student(self, student: Student) -> Student:
        raise NotImplementedError

    def add_result(self, result: Result) -> bool:
        raise NotImplementedError

    def get_results_by_student(self, student_id, only_last=True):
        raise NotImplementedError

    def get_results_by_course(self, course_id, only_last=True):
        raise NotImplementedError

    def close(self):
        self.conn.close()
