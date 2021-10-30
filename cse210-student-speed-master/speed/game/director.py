from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        words (list): List of the floating words on the screen.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer (Buffer): The current word being typed.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._words = []
        self._populate_words()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
         
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the letter typed and print it on the screen.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter(self._buffer)
        self._buffer.add_key_stroke(letter)
        for word in self._words:
            word.move_next()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_word_typed()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means updating the screen.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words)
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_word_typed(self):
        """Checkes if the characters typed correspond to the word. Updates the score and creates a new word.

        Args:
            self (Director): An instance of Director.
        """
        for word in self._words:
            word_sel = word.get_word()
            if word_sel in (self._buffer.get_buffer()):
                self._score.add_points(word.get_points())
                word.reset()
                break
     
    def _populate_words(self):
        """Description here"""
        
        for _ in range(constants.STARTING_WORDS):
            self._word = Word()
            self._words.append(self._word)
