from distutils.command.upload import upload
from django.db import models



# Create your models here.

class Urunler_Metal(models.Model):
    resim=models.ImageField()
    baslik=models.CharField(max_length=25)
    fiyat_eski=models.IntegerField()
    fiyat_guncel= models.IntegerField()
    resim = models.FileField(upload_to= 'filmler/', null = True)

    def __str__(self):
        return self.baslik

class Urunler_Metal_degil(models.Model):
    resim=models.ImageField()
    baslik=models.CharField(max_length=25)
    fiyat_eski=models.IntegerField()
    fiyat_guncel= models.IntegerField()
    resim = models.FileField(upload_to= 'filmler/', null = True)
    
    def __str__(self):
        return self.baslik
