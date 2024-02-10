from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BusTour, Cruise, Service
from .forms import FilterForm


# Create your views here.
def bustours_est(request):
    tours = BusTour.objects.filter(country='EST', category='BUS TOUR')

    if request.method == 'GET':
        form = FilterForm(data=request.GET)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = FilterForm(initial={'price': 500, 'duration': 1})

    return render(request, 'catalog/tours-list.html', {'tours': tours, 'form': form})


def bustours_lv(request):
    tours = BusTour.objects.filter(country='LV', category='BUS TOUR')

    if request.method == 'GET':
        form = FilterForm(data=request.GET)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = FilterForm(initial={'price': 500, 'duration': 1})

    return render(request, 'catalog/tours-list.html', {'tours': tours, 'form': form})


def bustours_lt(request):
    tours = BusTour.objects.filter(country='LT', category='BUS TOUR')

    if request.method == 'GET':
        form = FilterForm(data=request.GET)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = FilterForm(initial={'price': 500, 'duration': 1})

    return render(request, 'catalog/tours-list.html', {'tours': tours, 'form': form})


def bustours_ru(request):
    tours = BusTour.objects.filter(country='RU', category='BUS TOUR')

    if request.method == 'GET':
        form = FilterForm(data=request.GET)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = FilterForm(initial={'price': 500, 'duration': 1})

    return render(request, 'catalog/tours-list.html', {'tours': tours, 'form': form})


def cruises(request):
    tours = Cruise.objects.filter(category='CRUISE')

    if request.method == 'GET':
        form = FilterForm(data=request.GET)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = FilterForm(initial={'price': 500, 'duration': 1})

    return render(request, 'catalog/tours-list.html', {'tours': tours, 'form': form})


def bustour_page(request, pk):
    bustour = BusTour.objects.get(id=pk)
    return render(request, 'catalog/tour-page.html', {'tour': bustour})


def cruise_page(request, pk):
    cruise = Cruise.objects.get(id=pk)
    return render(request, 'catalog/tour-page.html', {'tour': cruise})


@login_required
def bustour_book(request, pk):
    bustour = BusTour.objects.get(id=pk)
    return render(request, 'catalog/tour-book.html', {'tour': bustour})

@login_required
def cruise_book(request, pk):
    cruise = Cruise.objects.get(id=pk)
    return render(request, 'catalog/tour-book.html', {'tour': cruise})



