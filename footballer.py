# import classes AttrDisplay and Pace_exception
from display import AttrDisplay
from pace_exception import Pace_exception


# create class Footballer
class Footballer(AttrDisplay):
    __type = 'Footballer'

    # make init footballer profile
    def __init__(self, name, pace=0, shooting=0, passing=0, dribbling=0, defending=0, physics=0):
        self.__name = name        # select footballer name
        minpace, maxpace = 0, 100 # select all player`s characteristic
        if minpace < pace < maxpace:  # speed check  
            self.pace = pace  
        else:
            raise Pace_exception(pace, minpace, maxpace)  # raise exception if failure speed check
        self.shooting = shooting
        self.passing = passing
        self.dribbling = dribbling
        self.defending = defending
        self.physics = physics
        self.__position = 'GOALKEEPER'  # make default football player position
        self.__idol_name = 'Cristiano Ronaldo'  # make default icon name

    # method to print the type of class
    @staticmethod
    def print_type():
        print(Footballer.__type)

    # function where we print all characteristics of player
    def characteristic(self):
        profile = []
        for key in self.__dict__:
            profile.append(f'{key}: {getattr(self, key)};')
            if key == 'physics':
                break
        del profile[0]
        print('My characteristic:')
        for key in profile:
            print(key)
        print()

    # make function to return the position of footballer(getter)
    @property
    def position(self):
        return self.__position

    # make function to select position - where footballer playing(setter)
    @position.setter
    def position(self, position):
        self.__position = position

    # function to return the name(getter)
    @property
    def name(self):
        return self.__name

    # function to return favourite football player(getter)
    @property
    def idol(self):
        return self.__idol_name

    # function to select favourite football player(setter)
    @idol.setter
    def idol(self, idol_name):
        self.__idol_name = idol_name

    # function footballer speaking about him
    def speak(self):
        print(f'I`m {self.__name} and I`m the best {self.__position} in the world!')


# classes Centre_back, Forward and Midfielder only for position
class Centre_back(Footballer):

    def __init__(self, name, pace=0, shooting=0, passing=0, dribbling=0, defending=0, physics=0):
        super().__init__(name, pace, shooting, passing, dribbling, defending, physics)
        self.position = 'CENTRE BACK'

    def training_defence(self):
        print(f'{self.name} train to take away balls different ways')


class Forward(Footballer):
    def __init__(self, name, pace=0, shooting=0, passing=0, dribbling=0, defending=0, physics=0):
        super().__init__(name, pace, shooting, passing, dribbling, defending, physics)
        self.position = 'FORWARD'

    def training_score(self):
        print(f'{self.name} train in shooting, pace and dribbling to score the goal')


class Midfielder(Footballer):
    def __init__(self, name, pace=0, shooting=0, passing=0, dribbling=0, defending=0, physics=0):
        super().__init__(name, pace, shooting, passing, dribbling, defending, physics)
        self.position = 'MIDFIELDER'

    def training_pass(self):
        print(f'{self.name} train to give the best passes')

# function where we can check object`s class 
'''def act(player):
    if isinstance(player, Centre_back):
        player.training_defence()
    elif isinstance(player, Midfielder):
        player.training_pass()
    elif isinstance(player, Forward):
        player.training_score()'''
