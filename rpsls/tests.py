# The rules of Rock-paper-scissors-lizard-Spock are:
# Scissors cut paper
# Paper covers rock
# Rock crushes lizard
# Lizard poisons Spock
# Spock smashes scissors
# Scissors decapitate lizard
# Lizard eats paper
# Paper disproves Spock
# Spock vaporizes rock
# Rock crushes scissors

# Tests are written to check game engine not views.

import unittest

from pyramid import testing


def _registerRoutes(config):
    config.add_route('home', '/')
    config.add_route('play', '/throw')


class ViewTests(unittest.TestCase):
    def setUp(self):
        import rpsls
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from .views import home_view
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        info = home_view(request)
        self.assertEqual(info['project'], 'RPSLS')

    def test_computer_gets_random(self):
        from .views import play
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        session = request.session
        session['win'] = 0
        session['lose'] = 0
        session['tie'] = 0
        request.params['sign'] = 'Rock'
        game = play(request)
        self.assertEqual(game['player_choice'], 'Rock')

    def test_player_win(self):
        from .views import play
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        session = request.session
        session['win'] = 0
        session['lose'] = 0
        session['tie'] = 0
        request.params['sign'] = 'Rock'
        game = play(request, comp_num=3)
        self.assertEqual(game['player_choice'], 'Rock')
        self.assertEqual(game['computer_choice'], 'Lizard')
        self.assertEqual(game['result'], 'Player wins!')
        self.assertEqual(game['explanation'], 'Rock crushes lizard!')

    def test_computer_win(self):
        from .views import play
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        session = request.session
        session['win'] = 0
        session['lose'] = 0
        session['tie'] = 0
        request.params['sign'] = 'Scissors'
        game = play(request, comp_num=1)
        self.assertEqual(game['player_choice'], 'Scissors')
        self.assertEqual(game['computer_choice'], 'Spock')
        self.assertEqual(game['result'], 'Computer wins!')
        self.assertEqual(game['explanation'], 'Spock smashes scissors!')

    def test_tie(self):
        from .views import play
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        session = request.session
        session['win'] = 0
        session['lose'] = 0
        session['tie'] = 0
        request.params['sign'] = 'Paper'
        game = play(request, comp_num=2)
        self.assertEqual(game['player_choice'], 'Paper')
        self.assertEqual(game['computer_choice'], 'Paper')
        self.assertEqual(game['result'], 'Player and computer tie!')
