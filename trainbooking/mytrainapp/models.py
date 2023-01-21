from django.db import models
from django.contrib import admin
# Create your models here.
class Train(models.Model):
    Trainno=models.IntegerField(primary_key=True, help_text="Trainno")
    Passengername=models.CharField(max_length=100)
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    Noofseat=models.IntegerField()
class Traininfo(admin.ModelAdmin):
    list_display = ("Trainno","Passengername","From","To","Noofseat")    