from django.db import models
from django.db.models.base import Model

# Create your models here.

class Workshop_form(models.Model):
    workshop_id = models.AutoField
    title = models.CharField(verbose_name="Workshop Title", max_length=100)
    desc = models.CharField(verbose_name="Description", max_length=2000)
    price = models.CharField(verbose_name="Price Per Entry", max_length=5)
    banner = models.ImageField(upload_to="static/workshops_images")
    slug = models.CharField(max_length=100, default="SLUG")

    def __str__(self):
        return self.title

class Enroll(models.Model):
    person_id = models.AutoField
    name = models.CharField(verbose_name="Full Name", max_length=70)
    email = models.EmailField(verbose_name="Email", max_length=70)
    wa_number = models.CharField(verbose_name="WhatsApp Number", max_length=15)
    ph_number = models.CharField(verbose_name="Calling Number", max_length=15)
    intro = models.CharField(verbose_name="Student Intro", max_length=700)
    tag = models.CharField(verbose_name="Tag", max_length=100)

    def __str__(self):
        return self.name + self.email 