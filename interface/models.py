from django.db import models
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    text_file = models.FileField(null=True,blank=True,validators=[FileExtensionValidator( ['txt'] ) ],)

class Entry(models.Model):
    name =   models.TextField(verbose_name="name",)
    gc_percentage = models.FloatField(verbose_name="percentage",max_length=5,default=00.00) 
    text_file = models.FileField(null=True,blank=True,validators=[FileExtensionValidator( ['txt'] ) ],)