from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home', renderer='home.jinja2')
def home_view(request):
    """
    Home view. Also initialize the scoreboard.
    """
     # Scoreboard with cookies :p
    session = request.session
    if not 'win' in session:
        session['win'] = 0
    if not 'lose' in session:
        session['lose'] = 0
    if not 'tie' in session:
        session['tie'] = 0

    return {'project': 'RPSLS'}



@view_config(route_name='play', renderer='result.jinja2')
def play(request, **kwargs):
    """
    A view function to play the game.
    Keyword arguments used for test purposes.
    """
    from .play_game import RPSLS, WIN, LOSE, TIE

    # Initialize the game engine
    game = RPSLS(request, **kwargs)

    # Play the game
    resp = game.play_game()

    # Update the scores
    session = request.session
    if resp['result'] == WIN:
        session['win'] += 1
    elif resp['result'] == LOSE:
        session['lose'] += 1
    else:
        session['tie'] += 1

    context = {
        'result': resp['result'],
        'player_choice': resp['player_choice'],
        'computer_choice': resp['computer_choice'],
        'win': session['win'],
        'lose': session['lose'],
        'tie': session['tie'],
        'project': 'RPSLS'
    }

    # Explanation messages for game result
    if resp['result'] != TIE:
        messages = {
            'ScissorsPaper': 'Scissors cut paper!',
            'ScissorsSpock': 'Spock smashes scissors!',
            'ScissorsRock': 'Rock crushes scissors!',
            'ScissorsLizard': 'Scissors decapitate lizard!',
            'PaperRock': 'Paper covers rock!',
            'RockLizard': 'Rock crushes lizard!',
            'LizardSpock': 'Lizard poisons Spock!',
            'LizardPaper': 'Lizard eats paper!',
            'PaperSpock': 'Paper disproves Spock!',
            'SpockRock': 'Spock vaporizes rock!',
        }
        try:
            context['explanation'] = messages[resp['player_choice']+resp['computer_choice']]
        except KeyError:
            context['explanation'] = messages[resp['computer_choice']+resp['player_choice']]

    else:
        context['explanation'] = ''

    return context


@view_config(route_name='reset')
def reset_score(request):
    """
    Self explanatory
    """
    session = request.session
    session['win'] = 0
    session['lose'] = 0
    session['tie'] = 0

    return HTTPFound('/')