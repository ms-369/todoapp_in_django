from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class task(models.Model):
   desc = models.CharField(max_length=1000)
   completed = models.BooleanField(default=False)
   
    