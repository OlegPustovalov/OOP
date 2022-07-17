class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self._av_grades = {}
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
# метод студент выставляет оценку лектору
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'
    def __str__(self):
         res = f'Студент \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._av_grades}' \
               f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses} \nОценки {self.grades}:'
         return res
 
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self._av_grades = {}
        self.grades = {}
class Lecturer(Mentor):     
    def __str__(self):
        res = f'Лектор \nИмя: {self.name} \nФамилия: {self.surname} \nЗакрепленные курсы: {self.courses_attached}'\
              f'\nСредняя оценка за лекции: {self._av_grades}'
        return res
class Reviewer(Mentor):
# метод Reviewer выставляет оценку студенту
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Ревьюер \nИмя: {self.name} \nФамилия: {self.surname} \nЗакрепленные курсы: {self.courses_attached}'
        return res
        
student_1 = Student('Александр', 'Соболев', 'male')
student_1.courses_in_progress += ['Python','Спартак']
student_1.finished_courses += ['Крылья Советов']
student_1.grades['Python']=10
student_1.grades['Спартак']=8
student_1._av_grades['Python']=9

student_2 = Student('Роман', 'Зобнин', 'male')
student_2.courses_in_progress += ['Git', 'Python','Спартак']
student_2.finished_courses += ['Динамо']
student_2.grades['Python']=9
student_2.grades['Спартак']=3
student_2._av_grades['Git']=8

reviewer_1 = Reviewer('Олег','Романцев')
reviewer_1.courses_attached += ['Git', 'Спартак']
reviewer_2 = Reviewer('Доменико','Тедеско')
reviewer_2.courses_attached += ['Python', 'Лейпциг']



lektor_1 = Lecturer('Андрей','Тихонов')
lektor_1.courses_attached += ['Git', 'Python','Спартак']
lektor_1._av_grades['Git']=8
lektor_2 = Lecturer('Валерий','Карпин')
lektor_2.courses_attached += ['Python','Спартак','Ростов']
lektor_2._av_grades['Python']=7

#reviewer_1.rate_hw(student_1, 'Python', 10)
#reviewer_1.rate_hw(student_2, 'Python', 10)
#reviewer_2.rate_hw(student_1, 'Python', 9)
#reviewer_2.rate_hw(student_2, 'Python', 8)
#student_1.rate_hw(lektor_1,'Python',9)
#student_1.rate_hw(lektor_2,'Python',9)

print(student_1)
print(student_2)
print(lektor_1)
print(lektor_2)
print(reviewer_1)
print(reviewer_2)


