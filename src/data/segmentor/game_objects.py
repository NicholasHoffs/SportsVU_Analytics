import pandas as pd

class Moment:
    """A class for keeping info about the moments"""
    def __init__(self, moment):
        self.quarter = moment[0]  # Hardcoded position for quarter in json
        self.game_clock = moment[2]  # Hardcoded position for game_clock in json
        self.shot_clock = moment[3]  # Hardcoded position for shot_clock in json
        ball = moment[5][0]  # Hardcoded position for ball in json
        self.ball = Ball(ball)
        players = moment[5][1:]  # Hardcoded position for players in json
        self.players = [Player(player) for player in players]

class Ball:
    """A class for keeping info about the balls"""
    def __init__(self, ball):
        self.x = ball[2]
        self.y = ball[3]
        self.radius = ball[4]
        self.color = '#ff8c00'  # Hardcoded orange

class Player:
    """A class for keeping info about the players"""
    def __init__(self, player):
        self.team = Team(player[0])
        self.id = player[1]
        self.x = player[2]
        self.y = player[3]
        self.color = self.team.color

class Constant:
    """A class for handling constants"""
    NORMALIZATION_COEF = 7
    PLAYER_CIRCLE_SIZE = 12 / NORMALIZATION_COEF
    INTERVAL = 10
    DIFF = 6
    X_MIN = 0
    X_MAX = 100
    Y_MIN = 0
    Y_MAX = 50
    COL_WIDTH = 0.3
    SCALE = 1.65
    FONTSIZE = 6
    X_CENTER = X_MAX / 2 - DIFF / 1.5 + 0.10
    Y_CENTER = Y_MAX - DIFF / 1.5 - 0.35
    MESSAGE = 'You can rerun the script and choose any event from 0 to '

class Team:
    """A class for keeping info about the teams"""

    color_dict = {
        1610612737: ('#E13A3E', 'ATL'),
        1610612738: ('#008348', 'BOS'),
        1610612751: ('#061922', 'BKN'),
        1610612766: ('#1D1160', 'CHA'),
        1610612741: ('#CE1141', 'CHI'),
        1610612739: ('#860038', 'CLE'),
        1610612742: ('#007DC5', 'DAL'),
        1610612743: ('#4D90CD', 'DEN'),
        1610612765: ('#006BB6', 'DET'),
        1610612744: ('#FDB927', 'GSW'),
        1610612745: ('#CE1141', 'HOU'),
        1610612754: ('#00275D', 'IND'),
        1610612746: ('#ED174C', 'LAC'),
        1610612747: ('#552582', 'LAL'),
        1610612763: ('#0F586C', 'MEM'),
        1610612748: ('#98002E', 'MIA'),
        1610612749: ('#00471B', 'MIL'),
        1610612750: ('#005083', 'MIN'),
        1610612740: ('#002B5C', 'NOP'),
        1610612752: ('#006BB6', 'NYK'),
        1610612760: ('#007DC3', 'OKC'),
        1610612753: ('#007DC5', 'ORL'),
        1610612755: ('#006BB6', 'PHI'),
        1610612756: ('#1D1160', 'PHX'),
        1610612757: ('#E03A3E', 'POR'),
        1610612758: ('#724C9F', 'SAC'),
        1610612759: ('#BAC3C9', 'SAS'),
        1610612761: ('#CE1141', 'TOR'),
        1610612762: ('#00471B', 'UTA'),
        1610612764: ('#002B5C', 'WAS'),
    }

    def __init__(self, id):
        self.id = id
        self.color = Team.color_dict[id][0]
        self.name = Team.color_dict[id][1]