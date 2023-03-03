from django.db import models

# Create your models here.
class Students(models.Model):
	name = models.CharField(max_length=10)
	phone_number = models.IntegerField(blank=True,null=True)
	first_name = models.CharField(max_length=10,blank=True,null=True)
	last_name = models.CharField(max_length=10,blank=True,null=True)
	e_mail = models.CharField(max_length=100,blank=True,null=True)
	gender = models.IntegerField(choices=status_choices,blank=True,null=True)