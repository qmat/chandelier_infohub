from django.core.management.base import BaseCommand, CommandError
from settings import *
from updates.models import Update
import dateutil.parser, pytz, gdata.docs.service, tweepy
from settings import TWITTER_PASS, TWITTER_USER, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET

SOURCE = "twitter"

class Command(BaseCommand):

    help = 'Retrieves tweets directed at @QMATChandelier.'

    def handle(self, *args, **options):

        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth)

        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')
        #tweets = api.search('@QMATChandelier')
        tweets = api.public_timeline()
        for tweet in tweets:
            if not updates or tweet.created_at > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = tweet.created_at
                new_update.author = tweet.from_user
                new_update.text = tweet.text
                new_update.save()