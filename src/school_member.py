#!/usr/bin/python
# -*- coding: utf-8 -*-


class Person(object):
    # name = ""
    # occupation = ""
    def __init__(self):
        self.name = ""
        self.occupation = ""

    def info(self):
        message = "Name: %s, occupation: %s" % (self.name, self.occupation)
        print(message)


class Teacher(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.name = "Teacher"
        self.occupation = "teacher"


class EnglishTeacher(Teacher):
    def __init__(self):
        super(Teacher, self).__init__()
        self.profession = "English"


class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        self.name = "Student"
        self.occupation = "student"


class ArtStudent(Student):
    def __init__(self):
        super(ArtStudent, self).__init__()
        self.profession = "Art"


class ScienceStudent(Student):
    def __init__(self):
        super(ScienceStudent, self).__init__()
        self.profession = "Science"


class Worker(Person):
    def __init__(self):
        super(Worker, self).__init__()
        self.name = "Worker"
        self.occupation = "worker"


class Factory(object):
    def produce(self, kind=None):
        self.product = self.create(kind)
        return self.product

    def create(self, kind):
        pass


class TeacherFactory(Factory):
    def create(self, kind=None):
        if kind is None:
            print("create a teacher.")
            return Teacher()
        elif kind == "english":
            print("create a %s teacher" % kind)
            return EnglishTeacher()
        else:
            print("wrong kind.")
            return None


class StudentFactory(Factory):
    def create(self, kind=None):
        if kind is None:
            print("create a student.")
            return Student()
        elif kind.lower() == "art":
            print("create a %s student." % kind)
            return ArtStudent()
        elif kind.lower() == "science":
            print("create a %s student." % kind)
            return ScienceStudent()
        else:
            print("wrong kind.")
            return None


class WorkerFactory(Factory):
    def create(self, kind=None):
        print("create a worker.")
        return Worker()


class AbstractFactory(object):
    def __init__(self, prod_type):
        self.prod_type = prod_type

    def factory(self):
        if self.prod_type.lower() == "teacher":
            return TeacherFactory()
        elif self.prod_type.lower() == "student":
            return StudentFactory()

if __name__ == "__main__":
    teacher_factory = TeacherFactory()
    student_factory = StudentFactory()
    worker_factory = WorkerFactory()

    teacher = teacher_factory.produce()
    teacher.info()

    english_teacher = teacher_factory.produce(kind="english")

    student = student_factory.produce()
    student.info()

    art_student = student_factory.produce(kind="art")
    science_student = student_factory.produce(kind="science")

    worker = worker_factory.produce()
    worker.info()

    # abstract factory?
    factory = AbstractFactory("teacher").factory()
    factory.produce()

