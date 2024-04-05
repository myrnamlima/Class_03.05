from otree.api import *



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'lists'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.StringField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['response']
    timeout_seconds = 20

    def vars_for_template(self):
        return {'time_left': self.subsession.get_remaining_time()}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.advance_to_results_page()

    def timeout_next_page(self):
        return Results  # Redirect to the Results page



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]