from django.db import models

class WebViewPreset(models.Model):
    name                  = models.CharField(max_length=512)
    views                 = models.IntegerField()
    urls                  = models.TextField()
    db_created            = models.DateTimeField(auto_now_add=1)

