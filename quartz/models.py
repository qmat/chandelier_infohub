from django.db import models

class QuartzSketch(models.Model):
    name                  = models.CharField(max_length=512)
    file                  = models.FileField(upload_to="quartz")
    db_created            = models.DateTimeField(auto_now_add=1)

