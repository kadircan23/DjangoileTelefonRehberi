from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.
class rehber(models.Model):
    name=models.CharField(max_length=120, verbose_name='Adı')
    surname=models.CharField(max_length=120, verbose_name='Soyadı')
    number=models.PositiveIntegerField(verbose_name='Tel No', validators=[RegexValidator(r'^\d{1,10}$')])
    address=models.TextField(max_length=120,verbose_name='Adresi')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('rehber:detail', kwargs={'id':self.id})

