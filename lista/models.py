from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)


#essa classe tem uma função que retorna o nome do item {
# }
    def __str__(self):
        return self.item

