from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    usex = models.CharField(max_length=100)
    uage = models.IntegerField()
    class Meta:
        db_table = 'user'