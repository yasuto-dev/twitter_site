from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    name = models.CharField("name", max_length=30)
    tweet = models.TextField("tweet", max_length=255)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.name    