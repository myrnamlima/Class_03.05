from os import environ


SESSION_CONFIGS = [
    dict(
        name='class_assignment', app_sequence=['class_assignment', 'payment_info'], num_demo_participants=6
    ),
    dict(
        name='rock_paper_scissors', display_name = 'Rock, Paper, and Scissors', app_sequence=['rock_paper_scissors', 'payment_info'], num_demo_participants=2
    ),
    dict(
         name='drawing_shapes',
         display_name='Geometrical drawing shapes',
         app_sequence=['geoms'],
         num_demo_participants=1,
    ),
dict(
         name='inputs',
         display_name='Here are different inputs for your application',
         app_sequence=['inputs'],
         num_demo_participants=1,
    ),
dict(
         name='sandwich',
         display_name='This is the sandwich task',
         app_sequence=['sandwich'],
         num_demo_participants=1,
    ),
    dict(
        name='regroup',
        display_name='group matrix manipulation',
        num_demo_participants=12,
        app_sequence=['regroup'],
    ),
    dict(
        name='sliders',
        display_name='example using UI sliders',
        num_demo_participants=1,
        app_sequence=['sliders'],
    ),
    dict(
        name='lists',
        display_name='UI with two linked and sortable lists',
        num_demo_participants=1,
        app_sequence=['lists'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
         name='live_demo',
         display_name='Room for live demo (no participant labels)',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '2248829945247'

INSTALLED_APPS = ['otree']
