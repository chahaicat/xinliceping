from django.db import models

# Create your models here.
class Userscore(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        db_table = 'userscore'