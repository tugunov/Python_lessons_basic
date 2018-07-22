# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, patr, surname):
        self.name = name
        self.surname = surname
        self.patr = patr
    def FIO(self):
        return '{} {} {}'.format(self.name, self.patr, self.surname)
    def get_initials(self):
        return '{} {}. {}.'.format(self.surname, self.name[0], self.patr[0])

class Teacher(Person): #родительским классом для Teacher будет Person
    def __init__(self, name,  patr, surname, subject):
        Person.__init__(self, name, patr, surname)
        self.subject = subject

class Class:
    def __init__(self, class_name, teachers):
        self._class_room = {'class_num': int(class_name.split()[0]), 'class_char': class_name.split()[1]}
        self.subj_teachers = {t.subject: t for t in teachers} # словарь предмет: учитель

    @property
    def class_name(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

class Student(Person): #родительским классом будет Person
    def __init__(self, name, surname, patr, class_name, parents):
        Person.__init__(self, name, surname, patr)
        self.class_name = class_name
        self.parents = parents

    def next_class(self):
        self._class_room['class_num'] += 1

teachers = [Teacher('Любовь', 'Чеславовна', 'Дулинец', 'математика'),
            Teacher('Валентина', 'Гарриевна', 'Угрехелидзе', 'русский язык'),
            Teacher('Екатерина', 'Львовна', 'Демиденко', 'литература'),
            Teacher('Борис', 'Викторович', 'Козулин', 'математика'),
            Teacher('Вера', 'Евгеньевна', 'Зайцева', 'биология'),
            Teacher('Софья', 'Васильевна', 'Ковалевская', 'математика'),
            Teacher('Николай', 'Александрович', 'Соловьев', 'русский язык'),
            Teacher('Адиля', 'Мамедовна', 'Дмитриева', 'химия')]

# заполнение структуры данных
classes = [Class('8 А', [teachers[0], teachers[2], teachers[4], teachers[7]]),
              Class('8 Б', [teachers[3], teachers[1], teachers[4], teachers[7]]),
              Class('9 А', [teachers[5], teachers[6], teachers[4], teachers[7]]),
              Class('9 В', [teachers[0], teachers[1], teachers[4], teachers[7]])]

parents = [Person('Виктор', 'Петрович', 'Яблоков'),
            Person("Вера", "Дмитриевна", "Яблокова"),
            Person('Николай', 'Ардалионович', 'Воронин'),
            Person('Анна', 'Петровна', 'Воронина'),
            Person('Анатолий', 'Иванович', 'Петров'),
            Person('Елена', 'Викторовна', 'Петрова'),
            Person('Михаил', 'Александрович', 'Скрипка'),
            Person('Елена', 'Львовна', 'Дмитриева'),
            Person('Леонид', 'Александрович', 'Обруч'),
            Person('Вера', 'Николаевна', 'Обруч'),
            Person('Валерий', 'Ильич', 'Перельман'),
            Person('Наталья', 'Александровна', 'Перельман'),
            Person('Михаил', 'Геннадьевич', 'Васильев'),
            Person('Любовь', 'Алексеевна', 'Васильева'),
            Person('Николай', 'Валентинович', 'Аверичев'),
            Person('Людмила', 'Анатольевна', 'Михайлова')]

students = [Student('Павел', 'Викторович', 'Яблоков', classes[0], [parents[0], parents[1]]),
            Student('Алексей', 'Николаевич', 'Воронин', classes[0], [parents[2], parents[3]]),
            Student('Иван', 'Анатольевич', 'Петров', classes[0], [parents[4], parents[5]]),
            Student('Галина', 'Михайловна', 'Скрипка', classes[1], [parents[6], parents[7]]),
            Student('Александр', 'Леондиович', 'Обруч', classes[1], [parents[8], parents[9]]),
            Student('Глеб', 'Валерьевич', 'Перельман', classes[2], [parents[10], parents[11]]),
            Student('Игорь', 'Михайлович', 'Васильев', classes[3], [parents[12], parents[13]]),
            Student('Екатерина', 'Николаевна', 'Аверичева', classes[3], [parents[14], parents[15]])]


print('Список классов школы') #1
for item in classes:
    print(item.class_name)

print('Список учеников {} класса'.format(classes[0].class_name)) #2
for item in [el.get_initials() for el in students if el.class_name == classes[0]]:
    print(item)
print('\n')

print('Список всех предметов ученика {}'.format(students[3].get_initials())) #3 пункт
for item in students[3].class_name.subj_teachers.keys():
    print(item)
print('\n')

print('ФИО родителей ученика {}'.format(students[5].get_initials())) #4 пункт
for parent in students[5].parents:
    print(parent.FIO())

print('\n')

print('Список учителей в классе', classes[0].class_name) #5
for teacher in classes[0].subj_teachers.values():
    print(teacher.FIO())

