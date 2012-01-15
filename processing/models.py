'''
Created on Jan 13, 2012

@author: vakkermans
'''

from django.db import models

class ProcessingSketch(models.Model):
    name                  = models.CharField(max_length=512)
    text                  = models.TextField()
    db_created            = models.DateTimeField(auto_now_add=1)

