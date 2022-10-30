from django.db import models

class Artiste(models.Model):
    """Information about an artiste in the app."""
    stage_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        """A string representation of the model"""
        return self.stage_name 

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()

class Lyrics(models.Model):
    content = models.CharField(max_length=10_000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
