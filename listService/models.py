from django.db import models

# Create your models here.


class ShopList(models.Model):
    shopList_name = models.CharField(max_length=100)


class ListElement(models.Model):
    item_name = models.CharField(max_length=100)
    shop_list = models.ForeignKey(ShopList, related_name='list_elements', default=1)

    def __str__(self):
        return self.item_name

