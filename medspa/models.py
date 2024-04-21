from django.db import models

class MedSpa(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    class Meta:
        db_table = 'medspa'

    def __str__(self):
        return self.name
