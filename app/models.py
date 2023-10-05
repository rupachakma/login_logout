from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=20)
    semester=models.CharField(max_length=20)
    address=models.TextField()
    phone=models.IntegerField()
    proimg=models.ImageField(upload_to="img",blank=True,null=True)

    def __str__(self):
        return self.name
