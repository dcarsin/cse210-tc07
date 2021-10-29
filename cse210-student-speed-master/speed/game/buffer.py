from game.actor import Actor
from game.point import Point
from game import constants


class Buffer(Actor):
    def __init__(self):
        self._buffer = ""
        super().__init__()
        self._points = 0
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")
    
    
    def get_buffer(self):
        return self._buffer

    def clear_buffer(self):
        self._buffer = ""

    def add_key_stroke(self, key_stroke):
        self._buffer += key_stroke
        self.set_text(f"Buffer: {self._buffer}")