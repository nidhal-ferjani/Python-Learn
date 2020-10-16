def pluralize(total, singular, plural=None):
    """
    :param total:
    :param singular:
    :param plural:
    :return:
    """
    try:
        assert str(total).isdigit() or isinstance(total, int)
    except AssertionError:
        print('total is not a number')
        return None
    else:
        if int(total) <= 0:
            print('Total doit être > 0')
            return None

        if not plural:
            plural = singular + 's'

        string = singular if int(total) <= 1 else plural
        return f'{total} {string}'
