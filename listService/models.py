from django.db import models

# Create your models here.


class ListElement(models.Model):
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
