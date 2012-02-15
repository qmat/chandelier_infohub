'''
N.B. Copy this file to settings_local.py and make the necessary changes.
'''

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/Users/someone/data/chandelier/infohub.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

GDOCS_USER  = "matstudentqmul"
GDOCS_PASS  = "XXXX"
GITHUB_USER = "qmat"
GMAIL_USER  = "qmatchandelier@gmail.com"
GMAIL_PASS  = "XXXX"
TWITTER_USER = "qmatchandelier"
TWITTER_PASS = "XXXX"
TWITTER_CONSUMER_KEY = "XXXX"
TWITTER_CONSUMER_SECRET = "XXX"
TWITTER_ACCESS_KEY = "XXX"
TWITTER_ACCESS_SECRET = "XXX"

ADMINS = (
    #('Your name', 'your@email.com'),
)

QUATZ_ADDRESS = 'tcp://127.0.0.1:10000'

MEDIA_ROOT = '/Users/someone/data/chandelier/media/'
