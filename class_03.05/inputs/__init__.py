from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'inputs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    offer = models.IntegerField(min=12, max=24) # for min and max
    level = models.IntegerField( # for drop-down answer
        choices=[(1, '1'), (2, '2'), (3, '3')],
    )
    level2 = models.IntegerField( # for drop-down answer
        choices=[
            [1, 'Low'],
            [2, 'Medium'],
            [3, 'High'],
        ]
    )
    radio = models.IntegerField( # for buttons
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3')
        ],
        widget=widgets.RadioSelect
    )
    pizza = models.IntegerField( # sliders
        widget=widgets.RadioSelect,
        choices=[-3, -2, -1, 0, 1, 2, 3]
    )




# PAGES
class MyPage1(Page):
    form_model = 'player'
    form_fields = ['offer','level','level2','radio','pizza']

    @staticmethod
    def vars_for_template(player):
        labels = {
            'offer_label': 'Enter a number between 12 and 24:',
            'level_label': 'Choose a level:',
            'level2_label': 'Choose a level:',
            'radio_label': 'Choose a level:',
        }
        return labels

class MyPage2(Page):

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage1, MyPage2 ResultsWaitPage, Results]
