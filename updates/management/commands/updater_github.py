'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.core.management.base import BaseCommand, CommandError
from github import github
from updates.models import Update
import dateutil.parser
import pytz

SOURCE = "github"

class Command(BaseCommand):

    help = 'Retrieves updates from the QMAT github.'


    def __interpret_date(self, date):
        # interpret date
        d = dateutil.parser.parse(date)
        # convert to UTC
        if d.tzinfo:
            d = d.astimezone(pytz.UTC)
            d = d.replace(tzinfo=None)
        return d


    def handle(self, *args, **options):
        # create a github handle
        gh = github.GitHub()

        # get the latest github update that's in the db
        updates = Update.objects.filter(source=SOURCE).order_by('-timestamp')

        # if there are no github updates in the db, just add all of them
        # if there are updates in the db already, check the date of the most recent one.
        for r in gh.repos.forUser(GITHUB_USER):
            most_recent_branch = False
            most_recent_branch_ts = False
            most_recent_commit = False
            for branchname, _ in gh.repos.branches(GITHUB_USER, r.name).items():
                commits = gh.commits.forBranch('qmat', r.name, branchname)
                # ignore the branch if there are no commits
                if not commits:
                    continue
                branch_ts = self.__interpret_date(commits[0].authored_date)
                # if it's the first check then take that one, otherwise compare
                if not most_recent_branch or branch_ts > most_recent_branch_ts:
                    most_recent_branch = branchname
                    most_recent_branch_ts = branch_ts
                    most_recent_commit = commits[0]
            # we now have the most recent branch
            if not updates or most_recent_branch_ts > updates[0].timestamp:
                new_update = Update()
                new_update.source = SOURCE
                new_update.timestamp = most_recent_branch_ts
                new_update.author = most_recent_commit.author.name
                new_update.text = "A change was committed to the %s repository on branch %s." % (r.name, most_recent_branch)
                new_update.save()




