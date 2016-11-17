# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    _species = 'Дракон'
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Troll(Enemy):
    _species = 'Тролль'
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer




class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 25
        self._color = 'черный'

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest

class FirstTroll(Troll):
    def __init__(self):
        self._health = 15
        self._attack = 10
        self._color = 'оранжевый'

    def question(self):
        x = randint(1, 3)
        self.__quest = 'Угадайте число от 1 до 3'
        self.set_answer(str(x))
        return self.__quest

class SimpleTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 25
        self._color = 'малиновый'

    def question(self):
        x = randint(1, 200)
        self.__quest = 'Число ' + str(x) + ' простое? (0 или 1)'

        def isprime(x):
            if x == 1:
                return '0'
            for i in range(2, x // 2):
                if x % i == 0:
                    return '0'

            return '1'

        self.set_answer(isprime(x))
        return self.__quest

class TrollTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 25
        self._color = 'утиный'



    def question(self):
        x = randint(3, 30)

        def func(n):
            Ans = []
            d = 2
            while d * d <= n:
                if n % d == 0:
                    Ans.append(str(d))
                    n //= d
                else:
                    d += 1
            if n > 1:
                Ans.append(str(n))
            return Ans


        self.__quest = 'Разложите число ' + str(x) + ' на множители и перечислите их через запятую'
        self.set_answer(','.join(func(x)))
        return self.__quest




        #FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, FirstTroll, SimpleTroll, TrollTroll]