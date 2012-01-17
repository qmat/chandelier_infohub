from django.db import models

class ProcessingSketch(models.Model):
    name                  = models.CharField(max_length=512)
    text                  = models.TextField()
    db_created            = models.DateTimeField(auto_now_add=1)

