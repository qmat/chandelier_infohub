'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.core.management.base import BaseCommand, CommandError
from updates.models import Update
import imaplib, dateutil.parser, pytz, sys

SOURCE = "gmail"

class Command(BaseCommand):

    help = 'Retrieves updates from the QMAT Chandelier gmail account.'


    def __interpret_date(self, date):
        # interpret date
        d = dateutil.parser.parse(date)
        # convert to UTC
        if d.tzinfo:
            d = d.astimezone(pytz.UTC)
            d = d.replace(tzinfo=None)
        return d


    def handle(self, *args, **options):
        conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        try:
            conn.login(GMAIL_USER, GMAIL_PASS)
        except:
            print sys.exc_info()[1]
            sys.exit(1)
        conn.select('Inbox') # Select inbox or default namespace
        retcode, messages = conn.search(None, '(UNSEEN)')
        if retcode == 'OK' and messages[0]:
            for message in messages[0].split(' '):
                print 'Processing :', message
                ret, mesginfo = conn.fetch(message, '(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])')
                if ret == 'OK':
                    # get the right bits out of the imap data
                    new_update = Update()
                    new_update.source = SOURCE
                    fields = mesginfo[0][1].split('\r\n')
                    for field in fields:
                        if field.startswith('Date: '):
                            new_update.timestamp = self.__interpret_date(field[len('Date: '):])
                        if field.startswith('From: '):
                            author = field[len('From: '):]
                            # filter out email address if a name was specified
                            bps = [author.find('<'), author.find('>')]
                            # do some sanity checking
                            if bps[0] < bps[1] and bps[0] >= 0 and bps[1] >= 0:
                                author = author[0:bps[0]-1]
                                author = author.strip("\"' ")
                            new_update.author = author
                        if field.startswith('Subject: '):
                            new_update.text = field[len('Subject: '):]
                    new_update.save()
            conn.store(messages[0].replace(' ',','),'+FLAGS','SEEN')
        conn.close()
