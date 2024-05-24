from django.db import models

# Create your models here.
"""Required fields include movie title, poster, description, release date, actors,
category and a YouTube trailer link."""
class Movieclub(models.Model):
  movie_title = models.CharField(max_length=255)
  poster = models.ImageField(upload_to='image/')
  description=models.CharField(max_length=1000)
  release_date=models.DateField()
  cast=models.CharField(max_length=1000)
  category=models.CharField(max_length=200)
  youtube_trailer_link=models.URLField(max_length=200)
  def __str__(self):
      return self.movie_title
