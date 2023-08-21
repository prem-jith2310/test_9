from django.db import models

# Create your models here.
class tbl_user(models.Model):
    uname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    place = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    class Meta:
        db_table = 'tbl_user'


class tbl_cake(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    flavour = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.CharField(max_length=200)
    class Meta:
        db_table = 'tbl_cake'      