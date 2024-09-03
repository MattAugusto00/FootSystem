from django.db import models

class Transfer(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    player = models.CharField(max_length=255)
    origin_club = models.CharField(max_length=255)
    destiny_club = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
      return self.player + " - " + self.destiny_club