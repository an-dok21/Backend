from django.db import models

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField()
    city = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = ('email', 'city')

    def __str__(self):
        return f'{self.email} - {self.city}'