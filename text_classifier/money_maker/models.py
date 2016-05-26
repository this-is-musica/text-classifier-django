from django.db import models


class Song(models.Model):
    lyrics = models.TextField()
    genre = models.CharField(max_length=32)


class Classifier(models.Model):
    classifier = models.BinaryField()
    counter = models.BinaryField()
    name = models.CharField(max_length=255, unique=True)
