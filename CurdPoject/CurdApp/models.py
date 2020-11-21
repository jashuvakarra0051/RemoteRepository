from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    email_id = models.EmailField()
    telugu = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()


