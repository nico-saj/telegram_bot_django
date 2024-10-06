from django.db import models

class Account(models.Model):
    name = models.TextField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
