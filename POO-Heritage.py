import  utils
class SportTeam(object):
    """
      This class has be generate BasketBall Teams
    """
    fine_amount = 50_000
    numbers_of_times = 0

    def __init__(self,name, wins, losses):
        self.__name = name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0

        """
        if self.__class__.__name__ == 'BasketBallTeam': # OR isinstance(self,classename)
            BasketBallTeam.numbers_of_times += 1
        elif self.__class__.__name__ == 'FootBallTeam':
            FootBallTeam.numbers_of_times += 1
        elif isinstance(self, SoccerTeam):
            SoccerTeam.numbers_of_times += 1"""

        # OR

        self.__class__.numbers_of_times += 1

        SportTeam.numbers_of_times += 1


    @property  # c'est un getter sur l'attribut name
    def name(self):
        print('je suis dans le getter de name')
        return self.__name

    @name.setter # c'est setter sur name
    def name(self, name):
        print('je suis dans le setter de name')
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None


    def get_fined(self):
        self.total_fines += self.fine_amount # on peut 'y acceder à un attribut de classe soit avec le nom de la classe
                                            # soit à travers un objet instance

    def stats(self):
        return f"{self.name} has {utils.pluralize(self.wins, 'victoire')} and {utils.pluralize(self.losses, 'défaite')}"


    #################################################################################################################
    #########  les Methodes de classes sont des bonnes techniques en python pour creer des Constructeurs additionnels
    #################################################################################################################

    @classmethod
    def set_fine_amount(cls, amount):
        print(cls)
        cls.fine_amount = amount # exactement comme EquipeBasketball.fine_amount

    @classmethod
    def from_file(cls, stats_as_file):
        try:
            with open(stats_as_file) as file:
                # print(file.readline().strip().split('-'))
                return cls.from_string( file.readline().strip())
        except FileNotFoundError:
            #raise ValueError('Stats File not Found.') from None # from None masque l'exception FileNotFoundError à l'affichage
            raise FileNotFoundError(f'Stats File {stats_as_file} not Found')from None



    @classmethod
    def from_string(cls, stats_as_string):
       # name, wins, losses = stats_as_string.split('-')
        return cls(*stats_as_string.split('-')) # or EquipeBasketball(name, wins, losses)

########################################################################################################################
################ les methodes static ne prend ni self ni cls dans python mais l'appel à cette methode ce fait avec
################ avec le mot self ou sur le nom de la classe : c'est methode utlitaire
########################################################################################################################
    @staticmethod
    def pluralize(total, singular, plural=None):
        """
        :param total:
        :param singular:
        :param plural:
        :return:
        """
        try:
            assert isinstance(total, int)
        except AssertionError:
            print('total is not a number')
            return None
        else:
             if total <= 0:
                 print('Total doit être > 0')
                 return None

             if not plural:
                 plural = singular + 's'

             string = singular if total <=1 else plural
             return f'{total} {string}'

#####################################################################################################################

class BasketBallTeam(SportTeam):

    numbers_of_times = 0
    fine_amount = 80_000

    def stats(self):
        return '[BASKETBALL] STATS: ' + super().stats()


class FootBallTeam(SportTeam):

    numbers_of_times = 0

    def __init__(self,name, wins, losses, draws=0):
        super().__init__(name, wins, losses)
        #OR
        #BasketBallTeam.__init__(self, name, wins, losses)

        self.draws = draws

    def stats(self):
        return f"{self.name} has {utils.pluralize(self.wins, 'victoire')}, {utils.pluralize(self.losses, 'défaite')} and  {utils.pluralize(self.draws, 'nul')}"


    """  @classmethod
    def from_string(cls, stats_as_string):
        name, wins, losses, draws = stats_as_string.split('-')
        return cls(name, int(wins), int(losses), int(draws)) # or EquipeBasketball(name, wins, losses)"""
    """@classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file) as file:
            # print(file.readline().strip().split('-'))
            return cls.from_string(file.readline().strip())"""


#####################################################################################################################
if __name__ == '__main__':
    print(help(BasketBallTeam))
    help(BasketBallTeam) # pareil comme SoccerTeam.__dict___

    team_1 = BasketBallTeam('Chigaco Bulls', 14, 25)
    team_11 = BasketBallTeam('Club', 14, 12)

    team_2 = FootBallTeam('Los angeles Likers', 27, 23)

    print("="*100)

    print(team_1.stats())
    print(team_2.stats())


    print(SportTeam.numbers_of_times)
    print(BasketBallTeam.numbers_of_times)
    print(FootBallTeam.numbers_of_times)

    print(team_1.total_fines)
    team_1.get_fined()
    print(team_1.total_fines)

    print(BasketBallTeam.numbers_of_times)

    print(team_2.total_fines)
    team_2.get_fined()
    print(team_2.total_fines)

    print(team_2.draws)

    team_22 = team_2.from_string("CSS SPORTIF-14-17-10")
    print(team_22.name,team_22.draws,team_22.wins,team_22.losses)
    print(team_22.draws)
    print(team_22.stats())

    print(FootBallTeam.from_file("equipe.txt").stats())

