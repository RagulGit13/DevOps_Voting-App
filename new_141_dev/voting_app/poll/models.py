from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    votes_1 = models.IntegerField(default=0)
    votes_2 = models.IntegerField(default=0)
    votes_3 = models.IntegerField(default=0)

    def total_votes(self):
        return self.votes_1 + self.votes_2 + self.votes_3

    def __str__(self):
        return self.question
