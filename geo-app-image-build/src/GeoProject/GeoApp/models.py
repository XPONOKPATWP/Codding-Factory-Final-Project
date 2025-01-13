from django.db import models
from django.utils import timezone


class UserQueryLogs(models.Model):
    username = models.CharField(max_length=100, default="Giorgos")
    query_city_1 = models.CharField(max_length=100, default="")
    query_city_2 = models.CharField(max_length=100, default="")
    coordinates_1 = models.CharField(max_length=100, default="(0.0,0.0)")
    coordinates_2 = models.CharField(max_length=100, default="(0.0,0.0)")
    result = models.FloatField(default=0.0)
    fuel_consumption = models.FloatField(default=0.0)
    calculated_distance = models.FloatField(default=0.0)
    is_kilometers = models.BooleanField(default=True)
    submition_date = models.DateTimeField(timezone.now, null=False, blank=False)

    def __str__(self):
        return self.username
