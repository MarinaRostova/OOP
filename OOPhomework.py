class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_student = grades_student
        student1 = Student("Ruoy", "Eman")
        student2 = Student()
    f'Имя: {self.name} \\nФамилия: {self.surname} \\nСредняя оценка за домашние задания: {self.rate_avg()} \\nКурсы в процессе изучения: {" | ".join(self.courses_in_progress)} \\nЗавершенные курсы: {" | ".join(self.finished\_courses)}'
    1234567891011

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


    student_1 = Student('Ruoy', 'Eman', 'female')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['Git']
    best_student.finished_courses += ['Введение в программирование']
    print(student_1)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

best_lecturer = Lecturer('Rona', 'Emana', 'your_gender')
best_lecturer.courses_in_progress += ['Python']

print(student1 <= student2)
print(student1 > student2)
print(student1 == student2)
print(student1)







cool_student = Student('Somet', 'Buddyes')
cool_student.courses_attached += ['Python']

cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)

print(best_lecturer.grades)





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.courses =[]
        self.grades_lecturer = grades_lecturer

    def __str__(self, name, surname, av_grades_lecturer):
        return f'{self, name, surname, av_grades_lecturer}'


sum_lecturer = 0
sum_grades = 0
count_lecture = 0

some_lecturer = Lecturer('Some', 'Buddy', '9.9')
some1_lecturer = Lecturer()
    for student in students:
          sum_lecture += sum(self.grades(course, []) / len(self.grades(course, [])
          count_lecture += 1
      result = av_grades_lecturer = round(sum_lecture / count_lecture, 1)
      return result


def _le_ (self, grades_lecturer):
        return some_lecturer <= some1_lecturer

def _gt_(self, grades_lecturer):
    return some_lecturer > some1_lecturer

def _eg_(self, grades_lecturer):
    return some_lecturer == some1_lecturer


print(some_lecturer <= some1_lecturer)
print(some_lecturer > some1_lecturer)
print(some_lecturer == some1_lecturer)
print(some_lecturer)





class Reviewer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self, name, surname):
        return f'{self, name, surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def str (self):
        return (f'Имя: {self.name} Фамилия: {self.surname}')
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer = Reviewer('Somer', 'Buddys')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(some_reviewer)





