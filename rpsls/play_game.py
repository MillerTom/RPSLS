import random

# Variables for result messages
WIN = "Player wins!"
LOSE = "Computer wins!"
TIE = "Player and computer tie!"


class RPSLS():
    """
    A small game engine for Rock - Paper - Scissors - Lizard - Spock
    Details are in README File.
    """

    def __init__(self, request, **kwargs):
        """
        Initializes the engine with necessary defaults,
        makes a random choice for computer and converts the player choice into a number.
        """
        # dictionary for signs
        self.names = {u'Rock': 0, u'Spock': 1, u'Paper': 2, u'Lizard': 3, u'Scissors': 4}
        # reverse dictionary for numbers
        self.numbers = {v: k for k, v in self.names.items()}

        # convert player_choice to a number to ease calculations.
        self.name = request.params['sign']
        self.player_number = self.names[self.name]

        # compute random guess for comp_number using random.randrange()
        # kwargs check for test purposes
        try:
            self.comp_number = kwargs['comp_num']
        except KeyError:
            self.comp_number = random.randrange(5)

        # initialize a dictionary for results
        self.results = {}

    def play_game(self):
        """
        Determines the winner according to the game logic,
        returns the results dictionary including player and computer choices.
        """
        difference = (self.player_number - self.comp_number) % 5
        if difference in [1, 2]:
            self.results['result'] = WIN
        elif difference == 0:
            self.results['result'] = TIE
        else:
            self.results['result'] = LOSE

        # convert comp_number to name using number_to_name static function,
        # add computer and player choices to results dictionary
        self.results['computer_choice'] = self.numbers[self.comp_number]
        self.results['player_choice'] = self.name

        return self.results