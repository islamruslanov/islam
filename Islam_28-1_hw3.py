class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory


    def __eq__(self, other):
        return self.__memory == other.__memory
    def __ne__(self, other):
        return self.__memory != other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __gt__(self, other):
        return self.__memory > other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory
    def __ge__(self, other):
        return self.__memory >= other.__memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value
    def make_computitatinos(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Процессор: {self.__cpu}  Память: {self.__memory} '


class Phone():
    def __str__(self):
        return self.call()
    __sim_card_list = ['o!', 'MegaCom', 'Beeline']

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number=int(input("Выберите сим-карту: ")), call_to_number=int(input("Введите номер: "))):
        if sim_card_number == 1:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[0]}"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[1]}"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} {self.__sim_card_list[2]}"


class SmartPhone(Computer,Phone):
    def __init__(self,cpu,memory):
        Computer.__init__(self,cpu,memory)



    def __str__(self):
        return super().__str__() + self.use_gps()

    def use_gps(self,locatoion=input('введите локации : ')):
        return f'был проложен от вашего место полажения до {locatoion} '

acer = Computer(5,248)
mi = Phone()
smartphone_1 = SmartPhone(4,128)
smartphone_2 = SmartPhone(4,128)
print(smartphone_1.use_gps())
print(smartphone_2.call())
print(acer)
print(mi)
print(smartphone_1)
print(smartphone_2)
print(acer.make_computitatinos())
print(acer != smartphone_1)
print(acer >= smartphone_2)
print(smartphone_1 < smartphone_2)



