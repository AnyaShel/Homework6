class Student:
    def __init__(self, name, surname, gender):
        self.average = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    #        self.average = float()

    def lecture_grade(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer) or course not in self.courses_in_progress \
                or course not in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mean_grade(self):
        meaning_grade = 0
        grade_count = 0
        for _grades in self.grades.values():
            meaning_grade += sum(_grades)
            grade_count += len(_grades)
        else:
            if meaning_grade:
                meaning_grade /= grade_count
        return meaning_grade

    def __str__(self):
        some_students = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {round(self.average, 1)}' \
              f'\nКурсы в процессе изучения: ', '.join(self.courses_in_progress)' \
              f'\nЗавершенные курсы: ', '.join(self.finished_courses)'
        return some_students

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Не студент!')
            return
        return self.average < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = float()

    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average = sum(map(sum, self.grades.values())) / grades_count
        some_lecturer = f'Имя: {self.name}' \
                        f'\nФамилия: {self.surname}' \
                        f'\nСредняя оценка за лекции: {round(self.average, 1)}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average < other.average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}' \
                        f'\nФамилия: {self.surname}'
        return some_reviewer


def lecturer_comparison(lecturer_list, course_name):
    begin = 0
    count_all_lecturer = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course_name]:
            begin += lecturer.average
            count_all_lecturer += 1
    average_for_all = begin / count_all_lecturer
    return round(average_for_all, 1)


def students_comparison(students_list, course_name):
    count_all_students = 0
    for student in students_list:
        if student.courses_in_progress == [course_name]:
            count_all_students += student.average
            count_all_students += 1
    average_for_all = count_all_students / count_all_students
    return round(average_for_all, 1)


student1 = Student('Tom', 'Holland', 'Male')
student2 = Student('Harri', 'Potter', 'Male')
lector1 = Lecturer('Sirius', 'Black')
lector2 = Lecturer('Severus', 'Snaip')
reviewer1 = Reviewer('Draco', 'Number One')
reviewer2 = Reviewer('Daniel', 'Number Two')

student1.finished_courses = ['Git']
student2.finished_courses = ['Python']
student1.courses_in_progress = ['Git', 'Python']
student2.courses_in_progress = ['Git', 'Python']
lector1.courses_attached = ['Git', 'Python']
lector2.courses_attached = ['Git', 'Python']
reviewer1.courses_attached = ['Git', 'Python']
reviewer2.courses_attached = ['Git', 'Python']

student1.lecture_grade(lector1, 'Python', 5)
student1.lecture_grade(lector2, 'Python', 4)
student2.lecture_grade(lector1, 'Python', 3)
student2.lecture_grade(lector2, 'Python', 4)

reviewer1.rate_hw(student1, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 4)

lector_list = {lector1, lector2}

student_list = {student1, student2}

if lector1 > lector2:
    print(f'У лектора {lector1.name} {lector1.surname} средняя оценка выше!')
elif lector1 == lector2:
    print(f'Средние оценки у лекторов {lector1.name} {lector2.surname} и {lector2.name} {lector2.surname} равны')
else:
    print(
        f'Средняя оценка у лектора {lector2.name} {lector2.surname} выше, чем у лектора {lector1.name} '
        f'{lector1.surname}')

if student1 > student2:
    print(
        f'У студента {student1.name} {student1.surname} средняя оценка выше, чем у студента '
        f'{student2.name} {student2.surname}')
elif student1 == student2:
    print(
        f'Средние оценки у студентов {student1.name} {student1.surname} и {student2.name} {student2.surname} равны')
else:
    print(
        f'Средняя оценка у студента {student2.name} {student2.surname} выше, чем у студента '
        f'{student1.name} {student1.surname}')


print(f"Средняя оценка всех лекторов по курсу {'Python'}: {lecturer_comparison(lector_list, 'Python')}")
print()

print(
    f"Средняя оценка за домашние задания всех студентов по курсу {'Git'}: {students_comparison(student_list, 'Git')}")
print()
