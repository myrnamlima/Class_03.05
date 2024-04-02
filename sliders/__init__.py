from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'sliders'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    value_1 = models.IntegerField()
    value_2 = models.IntegerField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['value_1', 'value_2']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]