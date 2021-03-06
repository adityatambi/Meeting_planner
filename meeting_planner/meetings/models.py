from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    floor_number=models.IntegerField(default=00)
    room_number=models.IntegerField(default=4)

    def __str__(self):
        return f"{self.name} on {self.floor_number} in {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
