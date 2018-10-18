from django.db import models
from django.contrib.postgres.fields import ArrayField


class Example(models.Model):
    simple_array = ArrayField(models.CharField(max_length=255))
