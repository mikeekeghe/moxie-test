import json
from django.db import models
from medspa.models import MedSpa

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    start_time = models.DateTimeField()
    total_duration = models.IntegerField()  # in minutes
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    medspa = models.ForeignKey(MedSpa, on_delete=models.CASCADE, related_name='appointments')
    services = models.JSONField()

    class Meta:
        db_table = 'appointment'

    def __str__(self):
        return f"Appointment at {self.start_time} for {self.medspa}"

    def save(self, *args, **kwargs):
        # Serialize services data before saving
        self.services = json.dumps(self.services)
        super().save(*args, **kwargs)

    def get_services(self):
        # Deserialize services data during retrieval
        return json.loads(self.services)
