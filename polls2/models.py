from django.db import models

class Document(models.Model):
    date = models.DateField(blank=True, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')