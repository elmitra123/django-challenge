from django.db import models
from django.contrib.auth.models import User


class Stadium(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Match(models.Model):
    firstteamname = models.CharField(max_length=200)
    secondteamname = models.CharField(max_length=200)
    date = models.DateTimeField()
    stadium = models.ForeignKey(Stadium, on_delete= models.CASCADE, related_name='matches')

    def __str__(self):
        return 'This match is between %s , %s in %s stadium' \
               %(self.firstteamname, self.secondteamname, self.stadium.name)


class Seat(models.Model):
    number = models.CharField(max_length=200)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='seats')
    is_full = models.BooleanField(default=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return 'This seat is places in %s for match between %s , %s with number : %s'\
               %(self.match.stadium.name, self.match.firstteamname, self.match.secondteamname, self.number)




