import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """ Description here """
    def __init__(self):
        """ Class constructor

            Args:

            _points (int): stores the count of points for the food
        """
        super().__init__()
        self._points = 0
        self._word = ''
        self.reset()
        
    def get_points(self):
        """ Method that returns the points """
        return self._points

    def reset(self):
        """ Description here """

        self._word = random.choice(constants.LIBRARY)
        self._points = len(self._word)
        self.set_text(self._word)
        x = random.randint(1, constants.MAX_X - 1)
        y = random.randint(1, constants.MAX_Y - 1)
        position = Point(x, y)
        velocity = Point(0, 1)
        self.set_position(position)   
        self.set_velocity(velocity)

    def get_word(self):
        """ Description here """
        return self._word