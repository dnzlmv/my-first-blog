import datetime
from django.db import models
from django.utils import timezone

class Frage(models.Model):
    frage_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.frage_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        


class Auswahl(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE)
    auswahl_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.auswahl_text
