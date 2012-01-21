'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.core.management.base import BaseCommand, CommandError
from updates.models import Update
import dateutil.parser, pytz, feedparser

SOURCE = "wiki"
FEED_URL = "http://qmat.net/wiki/index.php?title=Special:RecentChanges&feed=atom"

class Command(BaseCommand):

    help = 'Retrieves updates from the QMAT wiki through RSS.'

    def __interpret_date(self, date):
        # interpret date
        d = dateutil.parser.parse(date)
        # convert to UTC
        if d.tzinfo:
            d = d.astimezone(pytz.UTC)
            d = d.replace(tzinfo=None)
        return d


    def handle(self, *args, **options):
        articles = feedparser.parse(FEED_URL)['entries']
        # get the latest vimeo update timestamp=
        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')

        for article in articles:
            timestamp = self.__interpret_date(article['updated'])
            if not updates or timestamp > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = timestamp
                new_update.author = article['author']
                new_update.text = article['title']
                new_update.save()




