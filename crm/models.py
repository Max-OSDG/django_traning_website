from django.db import models

# Create your models here.
class Order(models.Model):
    order_data =  models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name= 'Имя пользователя')
    order_phone = models.CharField(max_length=20, verbose_name='номер телефона')

    def __str__(self):
        return self.order_name

 # class Meta:
 #    verbose_name = 'Заказ'
 #     #     # verbose_name_plural = 'Заказы'

