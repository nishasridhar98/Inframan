from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.



class Profile(models.Model):
	type_of_user=[('T','Tenant'),('O','Owner')]
	# title= models.ForeignKey(Property, on_delete=models.CASCADE)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	choice = models.CharField(max_length=1,choices=type_of_user,default='O')
	first_name = models.CharField(max_length=200,blank=True)
	last_name = models.CharField(max_length=200,blank=True)
	username = models.CharField(max_length=200)
	dob = models.DateField(blank=True, null=True)
	email = models.EmailField(max_length=70,blank=True)
	phone_number = models.CharField(max_length=12)


	def __str__(self):
		return f"{self.username} | {self.choice}" 


class Property(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField()
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} | {self.owner}"

	class meta:
		verbose_name='Properties'


class Tenant(models.Model):
	prop=models.ForeignKey(Property, on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	rent_date = models.DateField(blank=True, null=True)
	notify_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return f"{self.user.username} | {self.prop.name}" 



# class Invitation(models.Model):
# 	name = models.CharField(max_length=50)
# 	email = models.EmailField()
# 	code = models.CharField(max_length=20)
# 	sender = models.ForeignKey(User)

# 	def __unicode__(self):
# 		return u'%s, %s' % (self.sender.username, self.email)
