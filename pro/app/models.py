from django.db import models


class  Student(models.Model):
    name=models.CharField(max_length=100,verbose_name='الاسم')
    age = models.IntegerField(verbose_name='العمر')
    addrss=models.CharField(max_length=100,verbose_name='العنوان')
    def __str__(self):
        return self.name

