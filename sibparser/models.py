from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .parser import parser


def validatorNegative(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an positive number'),params={'value': value},)



"""
Модель в которой хранятся сайты которые должны распарситься, когда объект сохраняется в бд,
он так же создает поток, который запускается по timeshift
"""
class Site(models.Model):
    timeshiftSeconds = models.IntegerField(default=0, validators=[validatorNegative] )
    timeshiftMinutes = models.IntegerField(default=0)
    url = models.URLField()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        parser.threadStart(self)

    def __str__(self):
        return self.url



"""
Модель в которой храхятся уже обработанные сайты
"""
class ParsedSite(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=200, default=" ")
    encoding = models.CharField(max_length=20, default=" ")
    successfully = models.BooleanField(default=True)
    h1 = models.CharField(max_length=200)





