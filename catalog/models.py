from django.db import models
from datetime import date
from django.urls import reverse


# Define choices for Category field
BUSTOUR = 'BUS TOUR'
CRUISE = 'CRUISE'
# A list of tuples. First element of the tuple is an actual value
# to be set on the model field, and the second one is a human-readable name 
CATEGORY_CHOICES = [
    (BUSTOUR, 'Автобусный тур'),
    (CRUISE, 'Круиз'),
]

# Define choices for Country field 
EST = 'EST'
LV = 'LV'
LT = 'LT'
RU = 'RU'
COUNTRY_CHOICES = [
    (EST, 'Эстония'),
    (LV, 'Латвия'),
    (LT, 'Литва'),
    (RU, 'Россия'),
]


class TourDate(models.Model):
    tour_date = models.DateField(default=date.today, verbose_name='Дата тура')
    
    def __str__(self):
        return self.tour_date.strftime('%d %B %Y')


    def is_passed(self):
        return self.tour_date < date.today()


    class Meta:
        ordering = ['tour_date']
        db_table = 'Tour_date'
        verbose_name = 'Расписание тура'
        verbose_name_plural = 'Расписание туров'


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    notes = models.TextField(blank=True, verbose_name='Примечания')
    price = models.PositiveIntegerField(verbose_name='Цена')


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


# Abstract base class
# used to store general info about bus tours and cruises
class Tour(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(default='catalog_pics/tour-default-image.png',
                              upload_to='catalog_pics',
                              verbose_name='Путь к картинке')
    timeline = models.TextField(verbose_name='Программа тура')
    charges = models.TextField(verbose_name='Стоимость тура')
    price = models.PositiveIntegerField(verbose_name='Цена')
    n_days = models.PositiveIntegerField(default=1, verbose_name='Количество дней')
    group_size = models.PositiveSmallIntegerField(default=25, verbose_name='Количество мест')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=BUSTOUR, verbose_name='Категория')
    tourdates = models.ManyToManyField(TourDate, verbose_name='Даты тура')
    services = models.ManyToManyField(Service, blank=True, null=True, verbose_name='Услуги')

    def __str__(self):
        return self.title


    def get_tour_dates(self):
        """return days when the tour is happening"""
        tour_dates = self.tourdates.all()
        if tour_dates.exists():
            return tour_dates
        return []


    def get_services(self):
        services = self.services.all()
        if services.exists():
            return services
        return []

    
    class Meta:
        abstract = True
        ordering = ['title']


class BusTour(Tour):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=BUSTOUR, verbose_name='Категория')
    country = models.CharField(max_length=5, choices=COUNTRY_CHOICES, verbose_name='Страна')
    

    def get_absolute_url(self):
        """return the unique URL for each blog post"""
        return reverse('bus-tour', kwargs={'pk': self.pk})


    class Meta(Tour.Meta):
        db_table = 'Bus_tour'
        verbose_name = 'Автобусный тур' 
        verbose_name_plural = 'Автобусные туры'


class Ferry(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    link = models.URLField(blank=True, verbose_name='Ссылка на офиц. страницу')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Ferry'
        verbose_name = 'Паром'
        verbose_name_plural = 'Паромы'


class Cabin(models.Model):
    category = models.CharField(max_length=50, verbose_name='Класс каюты')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(default='catalog_pics/cabin-default-image.png',
                              upload_to='catalog_pics', verbose_name='Путь к картинке')
    price = models.PositiveIntegerField(verbose_name='Цена')
    n_passengers = models.SmallIntegerField(verbose_name='Число пассажиров')
    ferry = models.ForeignKey(Ferry, on_delete=models.CASCADE, related_name='cabins',verbose_name='Паром')

    def __str__(self):
        return f'{self.ferry.name}: {self.category}'


    class Meta:
        db_table = 'Cabin'
        verbose_name = 'Каюта'
        verbose_name_plural = 'Каюты'


CITIES_TO_COUNTRIES = {
    'Таллин': 'Эстония',
    'Рига': 'Латвия',
    'Хельсинки': 'Финляндия',
    'Стокгольм': 'Щвеция',
}


class Cruise(Tour):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CRUISE, verbose_name='Категория')
    ferry = models.ForeignKey(Ferry, on_delete=models.CASCADE, verbose_name='Паром')
    n_days = models.PositiveIntegerField(default=2, verbose_name='Количество дней')


    def get_absolute_url(self):
        """return the unique URL for each blog post"""
        return reverse('cruise', kwargs={'pk': self.pk})

    def get_countries(self):
        countries = ''
        city1, city2 = self.title.split(' - ')
        for key, val in CITIES_TO_COUNTRIES.items():
            if city1 == key:
                countries += val + ', '
            elif city2 == key:
                countries += val

        return countries


    class Meta(Tour.Meta):
        db_table = 'Cruise'
        verbose_name = 'Круиз'
        verbose_name_plural = 'Круизы'



