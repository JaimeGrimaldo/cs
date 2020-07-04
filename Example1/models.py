from django.db import models


class Example1(models.Model):
    name = models.CharField(max_length= 255, null = False)
    edad =models.IntegerField(null = False, default=1)
    direccion = models.CharField(max_length= 200, null = False, default = '')
    curp = models.CharField(max_length= 16,null = False, default = '')


    def __str__(self):
        return self.name,self.edad
    
    class Meta:
        db_table = 'Example1'