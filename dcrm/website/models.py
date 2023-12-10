from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    zipcode = models.CharField(max_length=15)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
