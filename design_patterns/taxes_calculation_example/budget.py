
class Budget(object):

    def __init__(self, value):

        self.__value = value

    # property definition
    @property
    def value(self):

        return self.__value
