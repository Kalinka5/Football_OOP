# create class Football_team
class Football_team:
    # make init name of the team and arguments from class Footballer
    def __init__(self, team_name, *args):
        self.team_name = team_name
        self.members = sorted(list(args), key=lambda self: self.__class__.__name__)

    # function where we add players in the team
    def add_player(self, footballer):
        self.members.append(footballer)

    # function where we show name of the team and all footballers which are belongs to
    def show_all(self):
        print(f'---THIS IS TEAM \'{self.team_name}\'---')
        for footballer in self.members:
            print(footballer)
        print()
        for footballer in self.members:
            footballer.speak()
            footballer.characteristics()