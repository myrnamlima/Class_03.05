import getopt

from otree.api import *
import random

doc = """
Rock, Paper, Scissors!
"""


class C(BaseConstants):
    NAME_IN_URL = 'rock_paper_scissors'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    CHOICES = ["Rock", "Paper", "Scissors"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    action = models.IntegerField()
    payout = models.IntegerField(initial = -999)
    type = models.IntegerField()


# functions
def creating_session(subsession):
    for p in subsession.get_players(): #this is collecting the player id and assigning them as column or row players
        if p.id_in_group % 2 == 0: # taking a number, dividing it by 2 and giving the remainder
            p.type = 1
        else:
            p.type = 2


def do_payoffs(g: Group):
    row_action = -999
    col_action = -999
    players = g.get_players()
    for p in players:
        if p.type == 1:   # this gives me the row action and column action that I am using to calculate payoffs
            row_action = p.action
        else:
            col_action = p.action


# PAGES
class Action(Page):
    form_model = 'player'
    form_fields = ['action']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'do_payoffs'
    body_text = "The other player is making a decision"


class Results(Page):
    pass


page_sequence = [Action, ResultsWaitPage, Results]
