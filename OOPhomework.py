class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.courses_attached = []



  def rate_lecturer(self, lector, course, grade):
      if (isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress
              and grade in range(0, 11)):
          if course in lector.grades:
              lector.grades[course] += [grade]
          else:
              lector.grades[course] = [grade]
      else:
          return 'Ошибка'

  def average_grade(self):
      result = 0
      if self.grades:
          for grade in self.grades.values():
              result += sum(grade) / len(grade)
          return result / len(self.grades)
      else:
          return 0

  def __str__(self):
      return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за домашние задания:"
              f"{self.average_grade()}\n Курсы в процессе изучения:{self.courses_in_progress}\n Завершенные курсы:"
              f"{self.finished_courses}")

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


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []
      self.grades = {}




class Lecturer(Mentor):

  def average_grade(self):
      result = 0
      if self.grades:
          for grade in self.grades.values():
              result += sum(grade) / len(grade)
          return result / len(self.grades)
      else:
          return 0

  def __str__(self):
      return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за лекцию:"
              f"{self.average_grade()}\n")



class Reviewer(Mentor):
  def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\n"

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'


best_student1 = Student('Ruoy', 'Eman', 'woman')
best_student2 = Student('Rick','Morty','male')
best_student3 = Student( 'Alf','Alfik', 'Ufo')

best_student1.finished_courses += ['Введение в програмирование']
best_student2.finished_courses += ['Введение в програмирование']
best_student3.finished_courses += ['Введение в програмирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

cool_lector = Lecturer('Some', 'Buddy')
cool_lector.courses_attached += ['Python', 'Git']




best_student1.courses_in_progress += ['Python', 'Git']
best_student2.courses_in_progress += ['Python', 'Git']
best_student3.courses_in_progress += ['Python', 'Git']

best_student1.rate_lecturer(cool_lector, 'Python',10)
best_student2.rate_lecturer(cool_lector, 'Python',10)
best_student3.rate_lecturer(cool_lector, 'Python',10)



cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student3, 'Python', 11)

cool_mentor.rate_hw(best_student1, 'Java', 4)
cool_mentor.rate_hw(best_student2, 'CSharp', 3)
cool_mentor.rate_hw(best_student3, 'C++', 10)

cool_mentor.rate_hw(best_student1, 'Java', 6)
cool_mentor.rate_hw(best_student2, 'Pascal', 8)
cool_mentor.rate_hw(best_student3, 'Java', 9)

print(cool_mentor)

print(cool_lector)

print(best_student1)





