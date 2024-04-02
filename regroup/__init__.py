from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'regroup'
    players_per_group = 3
    num_rounds = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    type = models.IntegerField()


# FUNCTIONS

def creating_session(s):

    # assign types to players

    for p in s.get_players():
        if p.id_in_group == 1:
            p.type = 'first_mover'
        else:
            p.type = 'second_mover'


    # randomly shuffle all second movers

    print('-----------------------------')
    print('round ' + str(s.round_number) + ' default group matrix')
    m = s.get_group_matrix() # rename the matrix given by otree
    print(m)

    ungrouped_second_movers = [] # create a list of ungrouped second movers

    for row in m: # I am saying here that I want to iterate the row in the matrix
        ungrouped_second_movers.append(row[1]) # getting the second element of the list [1,2,3]...
        ungrouped_second_movers.append(row[2]) # getting the third element of the list [1,2,3]...

    print('ungrouped_second_movers:  ', ungrouped_second_movers)

    new_m = [] # defining a new group matrix

    for row in m:
        p1 = row[0] # same from original m
        p2 = ungrouped_second_movers.pop(random.randrange(len(ungrouped_second_movers))) # the command is called popping, which is the same as sampling without replacement
        print('ungrouped_second_movers:  ', ungrouped_second_movers)

        p3 = ungrouped_second_movers.pop(random.randrange(len(ungrouped_second_movers))) # select one of the items, remove it and set it for p2
        print('ungrouped_second_movers:  ', ungrouped_second_movers) # printing out each time that we pop one of the elements

        new_m.append([p1, p2, p3]) # we pass through this loop 4 times and we add a new element to our new matrix
        print('new group matrix: ', new_m)

    s.set_group_matrix(new_m)

    print('round ' + str(s.round_number) + ' modified group matrix')
    print(s.get_group_matrix())
    # print('-----------------------------')















# def regroup(subsession):
#     for subses in [subsession.in_round(x) for x in range(1, Constants.num_rounds)]:
#         rnd = subses.round_number
#         mtx = subses.get_group_matrix()
#         print(rnd, mtx)
#         new_mtx = [[1],[2,3],[4,5,6]]
#         subses.set_group_matrix(new_mtx)
#         print(rnd, subses.get_group_matrix())





# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'regroup'


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]