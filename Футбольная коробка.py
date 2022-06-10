from colorama import init
from colorama import Fore
init()
 
class Footballer:
    def __init__(self, name, pace, shooting, passing, dribling, defending, physics):
        self.name = name
        self.pace = pace
        self.shooting = shooting
        self.passing = passing
        self.dribling = dribling
        self.defending = defending
        self.physics = physics
    
    def characteristics(self):
        self.dictionary = {}
        name_characteristics = ('Pace', 'Shooting', 'Passing', 'Dribling', 'Defending', 'Physics')
        characteristics = [self.pace, self.shooting, self.passing, self.dribling, self.defending, self.physics]
        result = zip(name_characteristics, characteristics)
        self.dictionary = dict(result)
        print(Fore.BLACK + 'My characteristics:')
        for key, value in self.dictionary.items():
            print(Fore.GREEN + f'{key}: {value}')
        print()
    
    def my_idol(self, name):
        print(Fore.RED + f'My favorite footballer is {name})')

class Centre_back(Footballer):
    position = 'CENTRE BACK'
    def speak(self):
        print(Fore.BLUE + f'I`m {self.name} and I`m the best {self.position} in the world!')
    
class Forward(Footballer):
    position = 'FORWARD'
    def speak(self):
        print(Fore.BLUE + f'I`m {self.name} and I`m the best {self.position} in the world!')
    
class Midfielder(Footballer):
    position = 'MIDFIELDER'
    def speak(self):
        print(Fore.BLUE + f'I`m {self.name} and I`m the best {self.position} in the world!')
        
danya = Centre_back('Kalina',70, 70, 60, 70, 70, 80)
eldar = Midfielder('Eldar',70, 40, 50, 40, 70, 80)
vanya = Midfielder('Krasavchyk',80, 70, 70, 70, 70, 80)
seriy = Forward('Seriy',90, 40, 60, 70, 30, 50)
egor = Centre_back('Egor',70, 60, 70, 70, 70, 80)
igor = Midfielder('Igorek', 80, 90, 80, 90, 60, 70)

seriy.speak()
seriy.characteristics()
igor.speak()
igor.characteristics()
vanya.speak()
vanya.characteristics()
eldar.speak()
eldar.my_idol('Krasavchyk')
eldar.characteristics()
danya.speak()
danya.my_idol('Lionel Messi')
danya.characteristics()
egor.speak()
egor.my_idol('Сергій Гріго')
egor.characteristics()
