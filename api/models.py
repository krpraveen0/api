from django.db import models

# Create your models here.

class Students(models.Model):
    s_no = models.IntegerField()
    s_name = models.CharField(max_length=60)
    s_course = models.CharField(max_length=60)
    course_fee = models.FloatField()
