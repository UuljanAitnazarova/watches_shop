from django.contrib.auth import get_user_model
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



class Order(models.Model):
    username = models.CharField(max_length=150, blank=False, null=False, verbose_name='Имя пользователя')
    phone_number = models.CharField(max_length=15, blank=False, null=False, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, blank=False, null=False, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    user = models.ForeignKey(get_user_model(), blank=True, null=True, related_name='order', on_delete=models.CASCADE)

    def __str__(self):
        return f'id: {self.pk} - username:{self.username}'


class ProductOrder(models.Model):
    product_id = models.ForeignKey('watches.Product', related_name='product_orders', on_delete=models.CASCADE)
    order_id = models.ForeignKey('watches.Order', related_name='product_orders', on_delete=models.CASCADE)
    units = models.IntegerField(verbose_name='Количество')


