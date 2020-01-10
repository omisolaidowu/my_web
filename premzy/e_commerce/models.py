from django.db import models
import os

class E_commerce(models.Model):
	product_name = models.CharField(max_length=200)
	details      = models.TextField(null=True)
	picture      = models.ImageField(upload_to='pictures', max_length=1000, blank=True)
	featured     = models.BooleanField(default=False)


class Register(models.Model):
	first_name   = models.CharField(max_length=150)
	middle_name  = models.CharField(max_length=150)
	last_name    = models.CharField(max_length=150)
	email        = models.EmailField(max_length=150)
	username     = models.CharField(max_length=150)
	password     = models.CharField(max_length=50)
	password1    = models.CharField(max_length=50)

# Create your models here.
