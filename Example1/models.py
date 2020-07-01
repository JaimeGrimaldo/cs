from django.db import models

# Create your models here.
class Example(models.Model):
    names = models.CharField(max_length = 255, null = False)
    def __str__(self):
        return self.names

    class Meta:
        db_table =  'Example'
        