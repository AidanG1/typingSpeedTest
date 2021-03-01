from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):  # model in place so implementing data save will be simple
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    passage = models.TextField()
    words_typed = models.PositiveIntegerField()
    passage_length = models.PositiveIntegerField()
    accuracy = models.FloatField()
    score = models.FloatField()
    characters_per_minute = models.FloatField()
    words_per_minute = models.FloatField()
