from footballer import Footballer, CentreBack, Midfielder, Forward


# create class Football_team
class FootballTeam:
    # make init name of the team and arguments from class Footballer
    def __init__(self, team_name, *args):
        self.team_name = team_name
        self.members = sorted(list(args), key=lambda member: self.__class__.__name__)

    # function where we add players in the team
    def add_player(self, footballer: Footballer):
        self.members.append(footballer)

    def training_pace(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_pace(6)
            elif isinstance(player, Midfielder):
                player.improve_pace(6)
            elif isinstance(player, Forward):
                player.improve_pace(6)

    def training_shooting(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_shooting(2)
            elif isinstance(player, Midfielder):
                player.improve_shooting(5)
            elif isinstance(player, Forward):
                player.improve_shooting(10)

    def training_passing(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_passing(7)
            elif isinstance(player, Midfielder):
                player.improve_passing(10)
            elif isinstance(player, Forward):
                player.improve_passing(3)

    def training_dribbling(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_dribbling(2)
            elif isinstance(player, Midfielder):
                player.improve_dribbling(7)
            elif isinstance(player, Forward):
                player.improve_dribbling(10)

    def training_defending(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_defending(10)
            elif isinstance(player, Midfielder):
                player.improve_defending(5)
            elif isinstance(player, Forward):
                player.improve_defending(2)

    def training_physics(self):
        for player in self.members:
            if isinstance(player, CentreBack):
                player.improve_physics(10)
            elif isinstance(player, Midfielder):
                player.improve_physics(5)
            elif isinstance(player, Forward):
                player.improve_physics(2)

    # function where we show name of the team and all footballers which are belongs to
    def show_all(self):
        print(f'---THIS IS TEAM \'{self.team_name}\'---')
        for footballer in self.members:
            print(footballer)
        print()
        for footballer in self.members:
            footballer.speak()
            footballer.print_idol()
            footballer.characteristic()
