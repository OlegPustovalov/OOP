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
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:         
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:        
                lector.grades[course] = [grade]
        else:
            print('Ошибка')
        summa = 0
        for el in lector.grades[course]:
            summa += el         
        lector._av_grades[course] = summa / len(lector.grades[course])
        
    def comp(self,student_other,course):
        av_grades1 = 0
        av_grades2 = 0
        if isinstance(student_other, Student) and course in self.courses_in_progress and course in student_other.courses_in_progress:
            av_grades1 = self._av_grades[course]
            av_grades2 = student_other._av_grades[course]
            if  av_grades1 > av_grades2:
                print (self.surname,' круче !') 
            elif av_grades1 == av_grades2:
                print (' боевая ничья !') 
            else:
                print (student_other.surname,' круче !') 
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
              
class Lecturer(Mentor):
#добавление к инициализации родительского класса grades,_av_grades через super()
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self._av_grades = {}
        
    def comp(self,lector_other,course):
        av_grades1 = 0
        av_grades2 = 0
        if isinstance(lector_other, Lecturer) and course in self.courses_attached and course in lector_other.courses_attached:
            av_grades1 = self._av_grades[course]
            av_grades2 = lector_other._av_grades[course]
            if  av_grades1 > av_grades2:
                print (self.surname,' круче !') 
            elif av_grades1 == av_grades2:
                print (' боевая ничья !') 
            else:
                print (lector_other.surname,' круче !')     
        
    def __str__(self):
        res = f'Лектор \nИмя: {self.name} \nФамилия: {self.surname} \nЗакрепленные курсы: {self.courses_attached}'\
              f'\nСредняя оценка за лекции: {self._av_grades} \nОценки {self.grades}:'
        return res
    

class Reviewer(Mentor):
# метод reviewer.rate_hw выставляет оценку студенту
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')
        summa2 = 0
        for el in student.grades[course]:
            summa2 += el         
        student._av_grades[course] = summa2 / len(student.grades[course])
        
    def __str__(self):
        res = f'Ревьюер \nИмя: {self.name} \nФамилия: {self.surname} \nЗакрепленные курсы: {self.courses_attached}'
        return res
#экземпляры класса студент        
student_1 = Student('Александр', 'Соболев', 'male')
student_1.courses_in_progress += ['Python','Спартак']
student_1.finished_courses += ['Крылья Советов']

student_2 = Student('Роман', 'Зобнин', 'male')
student_2.courses_in_progress += ['Git', 'Python','Спартак']
student_2.finished_courses += ['Динамо']

#экземпляры класса ревьюэр
reviewer_1 = Reviewer('Олег','Романцев')
reviewer_1.courses_attached += ['Python', 'Спартак']
reviewer_2 = Reviewer('Доменико','Тедеско')
reviewer_2.courses_attached += ['Python', 'Git']
#выставление оценок студентам
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Спартак', 7)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)
#экземпляры класса лекторы
lektor_1 = Lecturer('Андрей','Тихонов')
lektor_1.courses_attached += ['Python','Спартак']
lektor_2 = Lecturer('Валерий','Карпин')
lektor_2.courses_attached += ['Python','Спартак','Ростов']
# выставление оценок лекторам
student_2.rate_hw(lektor_1, 'Python', 10)
student_1.rate_hw(lektor_1,'Python', 8)
student_1.rate_hw(lektor_1,'Python', 5)
student_1.rate_hw(lektor_1,'Спартак', 5)
student_1.rate_hw(lektor_2,'Python', 7)
student_1.rate_hw(lektor_2,'Спартак', 8)
student_1.rate_hw(lektor_2,'Спартак', 10)
# печать магический метод _str_
print(student_1)
print(student_2)
print(lektor_1)
print(lektor_2)
print(reviewer_1)
print(reviewer_2)
#сравнение студентов по средним оценкам по определенному предмету
student_1.comp(student_2,'Python')
lektor_1.comp(lektor_2,'Python')
