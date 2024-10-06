from django.db import models

class Transaction(models.Model):
    class Status(models.TextChoices):
        OUTLAY = "outlay"
        INCOME = "income"

    status = models.TextField(choices=Status)
    created_at = models.DateField()

    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.status
