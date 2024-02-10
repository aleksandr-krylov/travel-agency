from django.db import models
from catalog.models import BusTour, Cruise, TourDate, Service, Cabin
from django.contrib.auth.models import User 
from django.urls import reverse
from itertools import chain


# Define choices for Category field
BUSTOUR = 'BUS TOUR'
CRUISE = 'CRUISE'
# A list of tuples. First element of the tuple is an actual value
# to be set on the model field, and the second one is a human-readable name 
CATEGORY_CHOICES = [
    (BUSTOUR, 'Автобусный тур'),
    (CRUISE, 'Круиз'),
]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    total = models.PositiveIntegerField(verbose_name='Итоговая сумма')
    date_started = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')


    def __str__(self):
        return f"Корзина {self.id}"

    
    def get_items(self):
        bustours = self.bustourcartitem_set.filter()
        cruises = self.cruisecartitem_set.filter()
        cart_items = sorted(
            chain(bustours, cruises),
            key=lambda instance: instance.date_booked.tour_date
        )

        return cart_items

    def items_count(self):
        return len(self.get_items())


    class Meta:
        db_table = 'Cart'
        verbose_name = 'Корзина' 
        verbose_name_plural = 'Корзины'

        
class CartItem(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=BUSTOUR, verbose_name='Категория')
    services = models.ManyToManyField(Service, blank=True, verbose_name='Услуги')
    date_booked = models.ForeignKey(TourDate, on_delete=models.CASCADE, verbose_name='Дата бронирования')
    subtotal = models.PositiveIntegerField(verbose_name='Сумма')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')


    class Meta:
        abstract = True
        ordering = ['date_booked']


class BusTourCartItem(CartItem):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=BUSTOUR, verbose_name='Категория')
    bustour = models.ForeignKey(BusTour, on_delete=models.CASCADE, related_name='bustours', verbose_name='Автобусный тур')
    

    def __str__(self):
        return f"{self.bustour.title}: {self.cart}"


    def get_remove_from_cart_url(self):
        return reverse('bustour-remove-from-cart', kwargs={'pk': self.pk})


    class Meta:
        db_table = 'Bus_tour_cart_item'
        verbose_name = 'Элемент корзины - автобусный тур' 
        verbose_name_plural = 'Элементы корзины - автобусные туры'


class CruiseCartItem(CartItem):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CRUISE, verbose_name='Категория')
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='cruises', verbose_name='Криуз')
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE, null=True, verbose_name='Каюта')


    def __str__(self):
        return f"{self.cruise.title} ({self.cart})"


    def get_remove_from_cart_url(self):
        return reverse('cruise-remove-from-cart', kwargs={'pk': self.pk})


    class Meta:
        db_table = 'Cruise_cart_item'
        verbose_name = 'Элемент корзины - круиз' 
        verbose_name_plural = 'Элементы корзины - круизы'

    