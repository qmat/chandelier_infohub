'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.db import models

class Update(models.Model):
    source                = models.CharField(max_length=512)
    author                = models.CharField(max_length=512)
    text                  = models.TextField()
    timestamp             = models.DateTimeField()
    db_created            = models.DateTimeField(auto_now_add=1)
