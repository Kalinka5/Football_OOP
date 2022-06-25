# import classes AttrDisplay and Football_team from files
from display import AttrDisplay
from football_team import Football_team

# create class Footballer
class Footballer(AttrDisplay):
    position = ''     # make position football player
    idol_name = ''

    # make init footballer name, pace, shooting, passing, dribling, defending and physics
    def __init__(self, name, pace=0, shooting=0, passing=0, dribling=0, defending=0, physics=0):
        self.name = name
        self.pace = pace
        self.shooting = shooting
        self.passing = passing
        self.dribling = dribling
        self.defending = defending
        self.physics = physics

    # make function position-where footballer playing
    def set_position(self, position):
        self.position = position

    # function where we print all characteristics of player
    def characteristics(self):
        attrs = []
        for key in self.__dict__:
            attrs.append(f'{key}: {getattr(self, key)};')
        del attrs[0]
        print('My characteristics:')
        for key in attrs:
            print(key)
        print()

    # function footballer speaking about him
    def speak(self):
        print(f'I`m {self.name} and I`m the best {self.position} in the world!')

# classes centre back, forward and midfielder only for position
class Centre_back(Footballer):
    position = 'CENTRE BACK'

class Forward(Footballer):
    position = 'FORWARD'

class Midfielder(Footballer):
    position = 'MIDFIELDER'

# if program name is main, execute code
if __name__ == '__main__':
    # create footballers and their characteristics
    danya = Centre_back('Kalina', 70, 70, 60, 70, 70, 80)
    eldar = Midfielder('Eldar', 70, 40, 50, 40, 70, 80)
    vanya = Midfielder('Krasavchyk', 80, 70, 70, 70, 70, 80)
    seriy = Forward('Seriy', 90, 42, 65, 70, 30, 50)
    egor = Centre_back('Egor', 70, 60, 70, 70, 70, 80)
    igor = Midfielder('Igorek', 80, 90, 80, 90, 60, 70)

    # create football team with football players what we created
    traders = Football_team('Traders', danya, eldar, vanya)
    brawlers = Football_team('Brawlers', seriy, egor, igor)
    # testing class football team
    traders.show_all()
    brawlers.show_all()



