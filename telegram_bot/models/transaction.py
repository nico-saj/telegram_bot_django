from django.db import models

class Transaction(models.Model):
    class Status(models.TextChoices):
        OUTLAY = "outlay"
        INCOME = "income"

    status = models.TextField(choices=Status)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    evaluated_at = models.DateTimeField()
    comment = models.TextField()

    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.status
