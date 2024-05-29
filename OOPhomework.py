class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self):
        return self.rate_hw

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Студент не принадлежит к классу Student'
        else:
            if self.rate_hw() > other.rate_hw():
                return f'Средний бал студента {self.name} {self.surname} лучше чем у студента {other.name} {other.surname}'
            elif other.rate_hw() > self.rate_hw():
                return f'Средний бал студента {other.name} {other.surname} лучше чем у студента {self.name} {self.surname}'
            else:
                return f'Студенты: {other.name} {other.surname} и {self.name} {self.surname} равнозначны по успеваемости'


    def _str_(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.rate_hw()} \nКурсы в процессе изучения: {" | ".join(self.courses_in_progress)} \nЗавершенные курсы: {" | ".join(self.finished_courses)}'

    some_student = Student('Ruoy', 'Eman', 'female')
    some_student.courses_in_progress += ['Python']
    some_student.courses_in_progress += ['Git']
    some_student.finished_courses += ['Введение в программирование']


    print(some_student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses = []
        self.courses_attached = []

class Lecturer (Mentor):


    def rate_avg(self):
        return self.rate_avg
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rate_avg()}'
    def av_grade_lecture(self, course, *students):
        if not isinstance(course, str):
            return "Ошибка"
    sum_lecturer = 0
    count_lecture = 0

    for student in students:
          sum_lecture += sum(self.grades(course, []))/ len(self.grades(course, []))
          count_lecture += 1
          result = round(sum_lecture / count_lecture, 1)
                return result



some_lecturer = Lecturer('Some', 'Buddy', '9.9')
some_lecturer.rate_avg(best_lecturer, 'Python', 10)
some_lecturer.rate_avg(best_lecturer, 'Python', 10)
some_lecturer.rate_avg(best_lecturer, 'Python', 10)

print(some_lecturer)





class Reviewer (Mentor):

    def __str__(self):
        return f'Имя: {self.name} \\nФамилия: {self.surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



some_reviewer = Reviewer('Some', 'Buddy')

some_reviewer.courses_attached += ['Python']


some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

print(some_reviewer)





