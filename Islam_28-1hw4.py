import random
from enum import Enum
from random import randint, choice


class SuperAdility(Enum):
    CRITICAL_DAMAGE = 1  # КРИТЕЧСКИЙ УРОН
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    BLOCK_A_BLOW = 5
    REVIVE = 6
    CALL_ANGEL_OR_CROW = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value >= 0:
            self.__health = value

        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f' {self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence  # зашита

    def Choose_defence(self, heroes):  # принимать зашиту
        hero = random.choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS' + super(Boss, self).__str__() + F' defece: {self.__defence} '


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):  # супер способность
        super(Hero, self).__init__(name, health, damage)
        if isinstance(ability, SuperAdility):
            self.__ability = ability
        else:
            ValueError('Wrong Date type for ability ')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAdility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior hits criticaly {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAdility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += random.randint(1, 20)


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAdility.HEAL)

        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAdility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            self.health -= boss.damage // 2
            self.__blocked_damage += boss.damage // 2
            self.damage += self.__blocked_damage


class Golem(Hero):
    def __init__(self, name, health, demage):
        super(Golem, self).__init__(name, health, demage, SuperAdility.BLOCK_A_BLOW)
        self.protection = 0

    def apply_super_power(self, boss, heroes):
        print(f"protection - {self.protection}")
        for hero in heroes:
            if hero.health > 0:
                self.protection = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.protection
                else:
                    hero.health -= boss.damage


class Witcher(Hero):
    def __init__(self, name, health, demage):
        super().__init__(name, health, demage, SuperAdility.REVIVE)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health += self.health
                self.health = 0


class Druid(Hero):
    def __init__(self, name, health, demage):
        super().__init__(name, health, demage, SuperAdility.CALL_ANGEL_OR_CROW)

    def apply_super_power(self, boss, heroes):
        angel_or_crow = random.choice([round_number])
        if angel_or_crow == 1:
            if boss.health < boss.health // 2:
                print("CALL TO CROW")
                boss.damage += boss.damage // 2

        elif angel_or_crow == 2:
            print('CALL TO ANGEL')
            for hero in heroes:
                hero.health += 10


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number}--------------')
    print(boss)

    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.Choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss != hero.ability:
            hero.attack(boss) and hero.health > 0
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start():
    boss = Boss('Rashan', 100000, 50)

    warrior = Warior('ahiles', 280, 10)

    doc = Medic('Estes', 250, 5, 15)
    magic = Magic('Merlin', 270, 15)
    berserk = Berserk('Thamus', 290, 10)
    assistant = Medic('Aibolit ', 290, 5, 5)
    golem = Golem('Golem', 400, 20, )
    witcher = Witcher('Witcher', 300, 0)
    druid = Druid('druid', 250, 25)

    heroes_list = [warrior, doc, magic, berserk, assistant, golem, witcher, druid]

    show_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start()

