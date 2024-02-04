# import classes Centre_back, Midfielder, Forward; Football_team and Pace_exception
from football_team import Football_team
from footballer import CentreBack, Midfielder, Forward
from pace_exception import PaceException


# if program name is main, execute code
if __name__ == '__main__':
    try:
        # create footballers and their characteristics
        danya = CentreBack('Kalina', 70, 70, 60, 70, 70, 80)
        danya.idol = 'Lionel Messi'
        eldar = Midfielder('Eldar', 70, 40, 50, 40, 70, 80)
        eldar.idol = 'Krasavchyk'
        vanya = Midfielder('Krasavchyk', 80, 70, 70, 70, 70, 80)
        seriy = Forward('Seriy', 90, 42, 65, 70, 30, 50)
        egor = CentreBack('Egor', 70, 65, 70, 75, 75, 80)
        egor.idol = 'Сергій Гріго'
        igor = Midfielder('Igorek', 80, 90, 80, 90, 60, 70)

        # create football team with football players what we created
        traders = Football_team('Traders', danya, eldar, vanya)
        brawlers = Football_team('Brawlers', seriy, egor, igor)
        # testing class football team
        traders.show_all()
        brawlers.show_all()
    #  if exception works, it should print Pace_exception
    except PaceException as e:
        print(e)
