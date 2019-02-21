from django.db import models

# Create your models here.
class Mom(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    phoneNumber=models.IntegerField(max_length=10)

    def __str__(self):
        return f'{self.f_name}{self.l_name}'

class Child(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    child_mom=models.ForeignKey(Mom,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.f_name}{self.l_name}'
