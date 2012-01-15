'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.core.management.base import BaseCommand, CommandError
from updates.models import Update
import dateutil.parser, pytz, urllib2, json

SOURCE = "vimeo"
VIMEO_CHANNEL_API_URI = "http://vimeo.com/api/v2/channel/247659/videos.json"

class Command(BaseCommand):

    help = 'Retrieves updates from the QMAT vimeo channel.'

    # we have to use a eastern time for vimeo
    def __interpret_date(self, date):
        # interpret date
        d = dateutil.parser.parse(date)
        d = d.replace(tzinfo=pytz.timezone('US/Eastern'))
        # convert to UTC
        d = d.astimezone(pytz.UTC)
        d = d.replace(tzinfo=None)
        return d


    def handle(self, *args, **options):
        videos = json.loads(urllib2.urlopen(VIMEO_CHANNEL_API_URI).read())

        # get the latest vimeo update timestamp=
        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')

        for video in videos:
            timestamp = self.__interpret_date(video['upload_date'])
            if not updates or timestamp > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = timestamp
                new_update.author = video['user_name']
                new_update.text = video['description']
                new_update.save()




