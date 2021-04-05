from django.db import models
from django.core.validators import MinValueValidator 

class Product(models.Model):

    CATEGORY_CHOICE = [
        ("men's_watches", "мужские часы"),
        ("ladies_watches", "женские часы"),
        ("couples'_watches", "парные часы"),
        ("other", "разное"),
    ]



    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, blank=False, null=False, default=CATEGORY_CHOICE[3], verbose_name='Категория')
    product_availability = models.IntegerField(validators=[MinValueValidator(0)],verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')


    def __str__(self):
        return self.name


class ProductCart(models.Model):
    product = models.ForeignKey('watches.Product', related_name='productcart', on_delete=models.CASCADE)
    units = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.product

