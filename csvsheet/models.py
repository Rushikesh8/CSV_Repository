from django.db import models

# Create your models here.
class Csv(models.Model):
    CSV_File = models.FileField(upload_to="csvsheet")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"