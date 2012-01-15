'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.core.management.base import BaseCommand, CommandError
from settings import *
from updates.models import Update
import dateutil.parser, pytz, gdata.docs.service

SOURCE = "gdocs"

class Command(BaseCommand):

    help = 'Retrieves updates from the QMAT google docs.'


    def __interpret_date(self, date):
        # interpret date
        d = dateutil.parser.parse(date)
        # convert to UTC
        if d.tzinfo:
            d = d.astimezone(pytz.UTC)
            d = d.replace(tzinfo=None)
        return d


    def handle(self, *args, **options):

        client = gdata.docs.service.DocsService()
        client.ClientLogin(GDOCS_USER, GDOCS_PASS)
        documents_feed = client.GetDocumentListFeed()

        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')

        for document_entry in documents_feed.entry:
            timestamp = self.__interpret_date(document_entry.updated.text)
            if not updates or timestamp > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = timestamp
                new_update.author = document_entry.lastModifiedBy.name.text
                new_update.text = document_entry.title.text
                new_update.save()

