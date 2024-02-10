from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from carts.models import Cart
from django.urls import reverse

# Create your models here.
class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50, verbose_name='Код оплаты')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Клиент')
    amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Сумма оплаты')
    date_paid = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')


    def __str__(self):
        return self.stripe_charge_id

        
class Order(models.Model):
    ref_code = models.CharField(max_length=10, unique=True, verbose_name='Код заказа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    total = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Итоговая сумма')
    date_ordered = models.DateField(default=timezone.now, verbose_name='Дата заказа')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Оплата')


    def __str__(self):
        return self.ref_code

    def get_order_done_url(self):
        return reverse('order-done', kwargs={'pk': self.pk})


    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ' 
        verbose_name_plural = 'Заказы'








