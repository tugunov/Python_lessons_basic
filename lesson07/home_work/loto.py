#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


import random
class Bag:
    def pick(self):
        onebyone = [x for x in range(1, self.number + 1)]
        random.shuffle(onebyone)
        for i, el in enumerate(onebyone):
            print('Вытащили бочонок: {}. В мешке осталось {} шт.'.format(el, self.number - i - 1))
            yield el #возвращаем генератор

    def __init__(self, number):
        self.number = number # количество бочонков
        self.gen = self.pick() # инициализируем генератор



class Game:
    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        # print('_setcard cards=', cards)
        random.shuffle(cards)
        
        while len(cards) % self.all_row != 0:
            cards.append('None')
        # print(cards)
        self.all_row = int(len(cards) / self.all_row)
        print(self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0,len(cards),self.all_row)]
        # список - список списков случайных последовательностей
        # print(cards)

        for i in range(len(cards)):
            cards[i].sort() # получаем последовательность для одной строки карточки
        self.human = cards[:3] # раздаем по три строчки игроку и компьютеру
        self.computer = cards[3:]


    def __init__(self, cards_number):
        rows = 3 # количество строк в карточке
        self.all_row = rows * cards_number
        self.__set_card()


    def get_card(self, player_card):
        print('----{}----'.format(self.name))
        print ('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}'.format(player_card[0]))
        print ('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}'.format(player_card[1]))
        print ('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}'.format(player_card[2]))
        print('----------------------------')


    def search_card(self, player_card, num_cask):
        for i, n in enumerate(player_card):
            if num_cask in n:
                player_card[i][n.index(num_cask)] = '-' # вычеркиваем число из карточки
                self.score += 1 # увеличиваем количество закрытых клеток
                if self.score == 15:
                    print('{} победил!'.format(self.name))
                    break
                return True # если нашли номер бочонка в карточке
        return False




class Player(Game):

    def __init__(self, name):
        self.name = name
        self.score = 0




game = Game(2)
cask = Bag(90)
player1 = Player('Человек')
player2 = Player('Компьютер')

input_flag = True # флаг корректности ввода пользователя
last_cask = 0

while True:
    if input_flag:
        num_cask = next(cask.gen) # печатаем номер следующего бочонка
        last_cask = num_cask
    else:
        print('Номер последнего бочонка: {}'.format(last_cask))
    player1.get_card(game.human) # печатаем текущее состояние карточек
    player2.get_card(game.computer)
    
    answer = input('Зачеркнуть цифру? (y/n)')
    if answer == 'y':
        input_flag = True
        if player1.search_card(game.human, num_cask): #нашли число и оно указано к зачеркиванию
            continue
        else:
            print('Вы проиграли') # зачеркивание отсутствующего на карточке числа
            break
    if answer == 'n':
        input_flag = True
        if player1.search_card(game.human, num_cask):
            print('Вы проиграли') # нашли число с бочонка в карточке после нажатия NO
            break
        elif player2.search_card(game.computer, num_cask):
            continue
    if answer != 'n' and answer != 'y':
        print('Введите y или n!')
        input_flag = False
        continue


