from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from itertools import chain
from django.views.generic.edit import DeleteView
from catalog.models import BusTour, Cruise, Service, TourDate, Cabin
from .models import Cart, BusTourCartItem, CruiseCartItem
from users.models import ADMIN, MANAGER, CLIENT


# Create your views here.
def bustour_add_to_cart(request, pk):
    bustour = get_object_or_404(BusTour, id=pk) # pull up the bustour
    # Double check for the user's status
    # Only clients can book tours and then add them to their carts
    if request.user.profile.status == CLIENT:
        request.session.set_expiry(120000) # session will expire in a half an hour
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            cart = Cart.objects.create(user=request.user, total=0)
            request.session['cart_id'] = cart.id
    else:
        messages.error(request, 'Ошибка! Для бронирования тура авторизуйтесь в системе в качестве клиента.')
        return redirect('/')
   
    if request.method == 'POST':
        try:
            date_booked = TourDate.objects.get(pk=request.POST['date']) 
        except:
            messages.error(request, 'Выберите дату бронирования тура.')
            return redirect('bustour-book', pk=pk)


        services_list = []
        for input_name in request.POST:
            if input_name.startswith('service'):
                service_id, _ = request.POST[input_name].split('-') 
                try:
                    s = Service.objects.get(pk=service_id)
                    services_list.append(s)
                except Service.DoesNotExist:
                    messages.error(request, 'Ошибка!')
                    redirect('bustour-book', pk=pk)
                

        cart_item, created = BusTourCartItem.objects.get_or_create(
            bustour=bustour,
            date_booked=date_booked,
            subtotal=bustour.price,
            cart=cart
        )

        if not created:
            messages.error(request, f'Атобусный тур "{bustour.title}" уже добавлен в корзину.')
            return redirect('bustour-book', pk=pk)

        for service in services_list:
            cart_item.services.add(service)
            cart_item.subtotal += service.price
        cart_item.save()

        messages.success(request, f'Автобусный тур "{bustour.title}" успешно добавлен в корзину.')
        return redirect('bustour-page', pk=pk)
        

def bustour_remove_from_cart(request, pk):
    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id) 
        except Cart.DoesNotExist:
            messages.error(request, 'Ошибка!')
            return redirect('/')

    cart_item = get_object_or_404(BusTourCartItem, id=pk) # pull up the cart item
    cart_item.delete()
    messages.success(request, f'Автобусный тур "{cart_item.bustour.title}" успешно удалён из корзины.')
    return redirect('cart')


def cruise_add_to_cart(request, pk):
    cruise = get_object_or_404(Cruise, id=pk) # pull up the cruise
    if request.user.profile.status == CLIENT:
        request.session.set_expiry(120000) # session will expire in a half an hour
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            cart = Cart.objects.create(user=request.user, total=0)
            request.session['cart_id'] = cart.id
    else:
        messages.error(request, 'Ошибка! Для бронирования тура войдите в систему в качестве клиента.')
        return redirect('/')
   
    if request.method == 'POST':
        try:
            date_booked = TourDate.objects.get(pk=request.POST['date']) 
        except:
            messages.error(request, 'Выберите дату бронирования тура.')
            return redirect('cruise-book', pk=pk)

        try:
            cabin_id, _ = request.POST['cabin'].split('-') 
            cabin = Cabin.objects.get(pk=cabin_id)
        except:
            messages.error(request, 'Ошибка!')
            return redirect('cruise-book', pk=pk)

        services_list = []
        for input_name in request.POST:
            if input_name.startswith('service'):
                service_id, _ = request.POST[input_name].split('-') 
                try:
                    s = Service.objects.get(pk=service_id)
                    services_list.append(s)
                except Service.DoesNotExist:
                    messages.error(request, 'Ошибка!')
                    redirect('cruise-book', pk=pk)

        cart_item, created = CruiseCartItem.objects.get_or_create(
            cruise=cruise,
            cabin=cabin,
            date_booked=date_booked,
            subtotal=cabin.price,
            cart=cart
        )

        if not created:
            messages.error(request, f'Круиз "{cruise.title}" уже добавлен в корзину.')
            return redirect('cruise-book', pk=pk)

        for service in services_list:
            cart_item.services.add(service)
            cart_item.subtotal += service.price
        cart_item.save()

        messages.success(request, f'Круиз "{cruise.title}" успешно добавлен в корзину.')
        return redirect('cruise-page', pk=pk)

    
def cruise_remove_from_cart(request, pk):
    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except Cart.DoesNotExist:
            messages.error(request, 'Ошибка!')
            return redirect('/')

    cart_item = get_object_or_404(CruiseCartItem, id=pk) # pull up the cart item
    cart_item.delete()
    messages.success(request, f'Круиз "{cart_item.cruise.title}" успешно удалён из корзины.')
    return redirect('cart')
    

def cart(request):
    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            context = {
            'empty': True
            }    
            return render(request, 'carts/cart.html', context) 

        new_total = 0
        for item in cart.get_items():
            new_total += item.subtotal
        cart.total = new_total
        cart.save()

        context = {
            'cart': cart
        }    
        return render(request, 'carts/cart.html', context)
       
    else:
        messages.error(request, 'Ошибка! Для бронирования тура авторизуйтесь в системе в качестве клиента.')
        return redirect('login')
        
        