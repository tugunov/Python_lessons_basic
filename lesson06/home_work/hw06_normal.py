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

class People:
    def __init__(self, name):
        self.name = name

    def get_full_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

class Classes:
	def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    def addStudent(self, student):
        # добавление ученика в класс
        self.students.append(student)
    def addTeacher(self, name, subject):
        # добавление учителя в класс
        self.teachers.append(Teacher(name, subject))
    def showClass(self):
        # метод для печати списка учеников класса
        print('Список учеников {} класса'.format(self.name))
        for itm in self.Pupils:
            print('ученик {}'.format(itm.name))

class Student(People, Classes):
    def __init__(self, name, class_room, father, mother):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name)
        Classes.__init__
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

class Teacher(People):
    def __init__(self, name, surname, birth_date, school, teach_classes):
        People.__init__(self, name)
        self.teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

class Parent(People): # для класса родителей учеников родительским классом будет People
    def __init__(self, name):
        People.__init__(self, name)
        self.teach_classes = 

