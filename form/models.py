from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	password = models.CharField(verbose_name='password',max_length=16)

	def __str__(self):
		return self.email
