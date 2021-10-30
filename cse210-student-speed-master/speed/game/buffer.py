from game.actor import Actor
from game.point import Point
from game import constants


class Buffer(Actor):
    """ Description here """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self._buffer = ""
        super().__init__()
        self._points = 0
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")
    
    
    def get_buffer(self):
        """Returns the string in the buffer.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        return self._buffer

    def clear_buffer(self):
        """Clears the buffer string
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self._buffer = ''

    def add_key_stroke(self, key_stroke):
        """Add the character typed by the user to the buffer string.
        
        Args:
            self (Buffer): an instance of Buffer.
            key_stroke (character): the character typed on the keyboard
        """
        self._buffer += key_stroke
        self.set_text(f"Buffer: {self._buffer}")