from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game import constants 

def get_number_words():
    """ 
        Ask the user to input the number of words on the screen. Check if the input is an integer, if not loop until it is.
    """
    while True:
        try:
            while constants.STARTING_WORDS < 1 or constants.STARTING_WORDS > 15:
                constants.STARTING_WORDS = int(input("How many words do you want on the screen to play (1-15)? "))
            break
        except ValueError:
            print('Invalid format. Please enter an integer.')
        
def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

get_number_words()
Screen.wrapper(main)