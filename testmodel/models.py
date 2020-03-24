from django.db import models

# Create your models here.


from django.db import models


class entrytask(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    account = models.IntegerField()
    submission_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'entrytask'
