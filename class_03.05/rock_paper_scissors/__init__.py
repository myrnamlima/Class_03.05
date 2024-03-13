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
    ACTIONS = ["Rock", "Paper", "Scissors"]
    PAYOFFS = [[[0,0],[-1,-1],[1,-1]],[[1,-1],[0,0],[-1,1]],[[-1,1],[1,-1],[0,0]]] #we want a list of tuples where each element is part of a sublist, this can be repeated for all 2 player games


class Subsession(BaseSubsession):
    round_number = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    action = models.IntegerField() #we can change this input button. Learn how...
    # payoff = models.IntegerField()
    type = models.IntegerField()
    opponent_action = models.IntegerField() #not for payoff calculations, just to show what was the other player's actions

# functions
def creating_session(subsession):
    for p in subsession.get_players(): #this is collecting the player id and assigning them as column or row players
        if p.id_in_group % 2 != 0: # taking a number, dividing it by 2 and giving the remainder
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

    for p in players:
        if p.type == 1: # player is type row
            p.payoff = C.PAYOFFS[row_action][col_action][0] #[row action][column action][inner most position of the payoffs]
            p.opponent_action = col_action
        else:
            p.payoff = C.PAYOFFS[row_action][col_action][1]
            p.opponent_action = row_action



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
