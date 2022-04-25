from django.db import models

class AddTextFile(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='File')
    unique_title = models.CharField(max_length=54, verbose_name='Unique title', null=True)
    unique_number = models.IntegerField(verbose_name='Unique number', null=True)
