from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	email = models.CharField(max_length = 100)
	bio = models.CharField(max_length = 500)
	profile_pic = models.ImageField(upload_to = 'profile_picture/')

	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'

	def __str__(self):
		return self.profile.user.username