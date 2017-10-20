from django.db import models

# Create your models here.


# let album Red has Primary key 1
class Artist(models.Model) :
    artist = models.CharField(max_length=250)
    artist_photo = models.FileField()

    def __str__(self):
        return self.artist

class Song(models.Model) :
    artist = models.ForeignKey(Artist , on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_file = models.FileField()
    song_size = models.IntegerField()
    song_length = models.FloatField()

    def __str__(self):
        return self.song_title