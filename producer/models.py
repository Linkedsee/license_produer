from django.db import models


class FunctionMapping(models.Model):
    function = models.CharField(max_length=200)
