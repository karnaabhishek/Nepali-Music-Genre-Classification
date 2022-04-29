from django.db import models

# Create your models here.
class Audio_store(models.Model):
    name = models.CharField(max_length=20)
    record = models.FileField(upload_to='')

    def __str__(self):
        return self.name