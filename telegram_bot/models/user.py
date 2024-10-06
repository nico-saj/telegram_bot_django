from django.db import models

class User(models.Model):
    user_telegram_id = models.IntegerField(unique=True)
    username = models.TextField()
    locale = models.TextField(null=True)

    def __str__(self):
        return self.username