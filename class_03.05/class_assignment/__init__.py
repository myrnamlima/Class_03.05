from otree.api import *


doc = """
This is for regrouping subjects during session
"""


class C(BaseConstants):
    NAME_IN_URL = 'class_assignment'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 5



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# Functions

def creating_session(s):
    if s.round_number == 2: # what I'm saying here is that it will reshuffle the number of participants only in round 2
     s.group_randomly() # if I just use this, I'm randomly assigning participants to different groups every round
    #if s.round_number > 2:
      #  s.group_like_round(2)




    #rnd = s.round_number
    #mtx = s.get_group_matrix()  # defines for every period, every matrix, for every subject
    #print(rnd, mtx)
    #new_mtx = [[1],[2,3],[4,5,6]]
    #s.set_group_matrix(new_mtx)
    #print(rnd,s.set_group_matrix())

   # if subsession.round_number >2:
      #  regroup(subsession)

#def regroup(subsession):
    #for subses in [subsession.in_round(x) for x in range(1, Constants.num_rounds)]:
        #rnd = subses.round_number
        #mtx = subses.get_group_matrix()
        #print(rnd, mtx)
        #new_mtx = mtx.dot(mtx)

# PAGES
class Action(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Action, ResultsWaitPage, Results]
