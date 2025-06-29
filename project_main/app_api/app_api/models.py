from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
