from django.core.management.base import BaseCommand, CommandError
from settings import *
from updates.models import Update
import dateutil.parser, pytz, gdata.docs.service, tweepy
from settings import TWITTER_PASS, TWITTER_USER

SOURCE = "twitter"

class Command(BaseCommand):

    help = 'Retrieves tweets directed at @QMATChandelier.'

    def handle(self, *args, **options):

        auth = tweepy.auth.OAuthHandler(TWITTER_USER, TWITTER_PASS)
        api = tweepy.API(auth)

        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')
        tweets = api.search('@QMATChandelier')

        for tweet in tweets:
            if not updates or tweet.created_at > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = tweet.created_at
                new_update.author = tweet.from_user
                new_update.text = tweet.text
                new_update.save()

