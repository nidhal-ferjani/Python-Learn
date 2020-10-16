#################################################################################################
############### invoke all keyword python  ######################################################
#################################################################################################
"""
import keyword

print(keyword.kwlist)"""

#################################################################################################
"""
a = 14

if 10<=a<=22:
    print("vrai")"""

###################################################################################################

def pluralize(total, singular, plural=None):
    """
    :param total:
    :param singular:
    :param plural:
    :return:
    """
    try:
        assert total.isdigit() or isinstance(total, int)
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



if __name__ == '__main__':
    print(__name__)
    print(pluralize(2, 'enfant'))

##################################################################################################