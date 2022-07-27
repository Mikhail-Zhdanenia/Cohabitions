# Cohabitation of two peoples with parameters
import random
Af = True

class Man:
    well_fed = 50

    def __init__(self, name, appetite, energy_spend, sallary, spending_ab, home=None):

        self.name = name
        self.appetite = appetite  # этот атрибут - сколько сьедает экземпляр
        self.energy_spend = energy_spend  # этот атрибут - сколько тратит энергии при работе
        self.sallary = sallary  # этот атрибут - сколько экземпляр зарабатывает
        self.spending_ab = spending_ab  # этот атрибут - сколько экземпляр тратит
        self.home = home  # наличие дома
        self.home.hobbits_list.append(self)


    def __str__(self):
        return f'{self.name} parameters:\n-appetite-{self.appetite}\n-energy spending at work - {self.energy_spend}\n' \
               f'-work sallary - {self.sallary}\n-shopping spending - {self.spending_ab}\n{self.home}\n'

    def eat(self):
        self.well_fed += 1
        self.home.food -= self.appetite

    def work(self):
        self.well_fed -= self.energy_spend
        self.home.money += self.sallary

    def play(self):
        self.well_fed -= 5

    def shopping(self):
        self.home.money -= self.spending_ab
        self.home.food += 10


    def act(self):
        param_choise = random.randint(1, 6)
        if self.well_fed < 0:
            raise ValueError
        else:
            if self.well_fed < 20:
                self.eat()
            elif self.home.food < 10:
                self.shopping()
            elif self.home.money < 50:
                self.work()
            elif param_choise == 1:
                self.work()
            if param_choise == 2:
                self.eat()
            elif param_choise == 3:
                self.work()
            if param_choise == 4:
                self.eat()
            elif param_choise == 5:
                self.play()
            elif param_choise == 6:
                self.shopping()
            else:
                self.play()

class House:

    def __init__(self):

        self.food = 50
        self.money = 0
        self.hobbits_list = list()

    def __str__(self):
        return f'House: food_stock - {self.food}, money_stock - {self.money}, hobbits inside - {self.hobit_count()}.'

    def hobit_count(self):
        return len(self.hobbits_list)

print('Life wrestling experiment.\n')

house = House()

djohny = Man('Djohn', random.randint(0, 10), random.randint(10, 15), random.randint(10, 25),
             random.randint(5, 15), home=house)
ilona = Man('ilona', random.randint(0, 7), random.randint(7, 12), random.randint(10, 15),
            random.randint(10, 20), home=house)

print(djohny)
print(ilona)

for day in range(1, 366):
    try:
        house.hobbits_list[random.randint(0, house.hobit_count() - 1)].act()
    except ValueError:
        print(f'D-day is {day}, shit happens( Someone dead! {djohny.well_fed}')
        break
else:
    print('365 days is done.')

