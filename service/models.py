from django.db import models
from appointment.models import Appointment
from medspa.models import MedSpa

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    medspa = models.ForeignKey(MedSpa, on_delete=models.CASCADE, related_name='services')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='service_instances', null=True)

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name
