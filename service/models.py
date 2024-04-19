from django.db import models
from medspa.models import MedSpa

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    medspa = models.ForeignKey(MedSpa, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name
