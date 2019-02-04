from djongo import models
from django.contrib.auth.models import User

class TimeStamp(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Interest(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True)
    path = models.CharField(max_length=255, null=True)
    interest_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    audience_size = models.IntegerField(null=True)

class Region(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    region_id = models.IntegerField(unique=True)
    region = models.CharField(max_length=255, null=True)
    country_code = models.CharField(max_length=16, null=True)
    country_name = models.CharField(max_length=255, null=True)
