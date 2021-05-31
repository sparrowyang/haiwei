from django.db import models


class food(models.Model):
    id = models.AutoField(primary_key=True)
    imgid_1 = models.ImageField(upload_to='photos', default='avatar.jpg')
    # imgid_2 = models.ImageField(upload_to='', default='avatar.jpg', blank=True)
    location = models.CharField(max_length=20)
    wname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    price = models.IntegerField()
    taste = models.CharField(max_length=999)
    others = models.CharField(max_length=999, null=True)
