from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.TextField() # 4I-IN1:TD
    description = models.TextField() # BUREAU D
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title
