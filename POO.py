
import  utils
class EquipeBasketball(object):
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

        EquipeBasketball.numbers_of_times += 1

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
        self.total_fines += self.fine_amout # on peut 'y acceder à un attribut de classe soit avec le nom de la classe
                                            # soit à travers un objet instance

    def stats(self):
        return f"[BASKETBALL] STATS: {self.name}: {utils.pluralize(self.wins, 'victoire')} - {utils.pluralize(self.losses, 'défaite')}"


    #################################################################################################################
    #########  les Methodes de classes sont des bonnes techniques en python pour creer des Constructeurs additionnels
    #################################################################################################################

    @classmethod
    def set_fine_amount(cls, amount):
        print(cls)
        cls.fine_amount = amount # exactement comme EquipeBasketball.fine_amount

    @classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file) as file:
           # print(file.readline().strip().split('-'))
            name, wins, losses = file.readline().strip().split('-')
            return cls(name, int(wins), int(losses))


    @classmethod
    def from_string(cls, stats_as_string):
        name, wins, losses = stats_as_string.split('-')
        return cls(name, int(wins), int(losses)) # or EquipeBasketball(name, wins, losses)

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

import os

if __name__ == "__main__":


    team_1 = EquipeBasketball('Chigaco Bulls', 14, 25)

    team_2 = EquipeBasketball('Los angeles Likers', 27, 23)


    print(EquipeBasketball.__dict__)
    print(dir(EquipeBasketball))
    print(EquipeBasketball.__doc__)
    print(team_1.__dict__)
    print(dir(team_2))

    print(team_2.stats())

    print(EquipeBasketball.stats(team_1))

    print("="*100)

    print(EquipeBasketball.__dict__)
    print(team_1.__dict__)
    print(team_2.__dict__)

    print("="*100)
    print(team_1.numbers_of_times)
    print(team_2.numbers_of_times)
    EquipeBasketball.set_fine_amount(15_000)
    print(EquipeBasketball.fine_amount)
    print(team_2.fine_amount)
    print(team_1.fine_amount)
    ######################################################################################################
    print(team_1.stats())
    # or c'esst pareil
    print(EquipeBasketball.stats(team_1))
    #####################################################################################################

    team_1.set_fine_amount(78_000)
    print(EquipeBasketball.fine_amount)

    raptors_stats = 'Toronto Raptors-36-14'

    print(EquipeBasketball.from_string(raptors_stats).stats())
    print(EquipeBasketball.from_file('milwaukee.txt').stats())

    print(team_1.name)
    team_1.name = 'nidhal'
    del team_1.name
    print(team_1.stats())
