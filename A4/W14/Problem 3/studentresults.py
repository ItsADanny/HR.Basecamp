from result import Result
from student import Student
from course import Course
from resultsmanager import ResultsManager


if __name__ == "__main__":
    manager = ResultsManager()
    manager.create_tables()

    dev101 = manager.get_course(1)

    if not dev101:
        dev101 = manager.add_course(Course("Development 101", 4))

    john = manager.get_student(1)

    print(john)

    if not john:
        john = manager.add_student(Student("John", "Doe", "2003-08-12", "BC11A"))
        manager.add_result(Result(john.id, dev101.id, 50, "2023-03-18"))
        manager.add_result(Result(john.id, dev101.id, 40, "2023-05-05"))  # should not be added
        manager.add_result(Result(john.id, dev101.id, 70, "2023-06-22"))

    print(john)

    print(john)

    print(manager.get_results_by_student(john.id))

    print(manager.get_results_by_course(dev101.id, False))

    manager.close()
