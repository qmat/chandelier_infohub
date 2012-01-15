'''
N.B. Don't add this file to the repository, as it contains passwords and other
     sensitive data!
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
