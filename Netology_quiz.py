class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод для расчета средней оценки за домашние задания
    def calculate_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Метод __str__ для вывода информации о студенте
    def __str__(self):
        average_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    # Метод для сравнения студентов по средней оценке
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return "Ошибка: Сравнение возможно только между студентами"

    # Метод для выставления оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Метод для расчета средней оценки за лекции
    def calculate_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Метод __str__ для вывода информации о лекторе
    def __str__(self):
        average_grade = self.calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"

    # Метод для сравнения лекторов по средней оценке
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return "Ошибка: Сравнение возможно только между лекторами"


class Reviewer(Mentor):
    # Метод для выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Метод __str__ для вывода информации о ревьюере
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функция для подсчета средней оценки за домашние задания по всем студентам на курсе
def calculate_average_student_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0


# Функция для подсчета средней оценки за лекции всех лекторов на курсе
def calculate_average_lecturer_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0


# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['JavaScript']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Another', 'Person')
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('First', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Second', 'Reviewer')
reviewer2.courses_attached += ['Git']

# Вызываем методы для ревьюеров
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student2, 'Git', 6)

# Вызываем методы для студентов
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 7)

# Создаем списки студентов и лекторов
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

# Вызываем функции для подсчета средних оценок
average_student_grade_python = calculate_average_student_grade(students_list, 'Python')
average_lecturer_grade_python = calculate_average_lecturer_grade(lecturers_list, 'Python')

# Выводим информацию через __str__
print("=== Информация о студентах ===")
print(student1)
print()
print(student2)
print()

print("=== Информация о лекторах ===")
print(lecturer1)
print()
print(lecturer2)
print()

print("=== Информация о ревьюерах ===")
print(reviewer1)
print()
print(reviewer2)
print()

# Сравниваем студентов
print("=== Сравнение студентов ===")
print(student1 > student2)  # True, если средняя оценка student1 выше
print(student1 == student2)  # False
print()

# Сравниваем лекторов
print("=== Сравнение лекторов ===")
print(lecturer1 > lecturer2)  # True, если средняя оценка lecturer1 выше
print(lecturer1 == lecturer2)  # False
print()

# Выводим средние оценки
print("=== Средние оценки ===")
print(f"Средняя оценка за домашние задания по курсу Python: {average_student_grade_python:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecturer_grade_python:.1f}")