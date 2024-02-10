from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import ClientProfile, CLIENT
from carts.models import Cart
from .models import Order
from users.forms import UserUpdateForm, ClientUpdateForm, PassportForm
from .utils import refcode_generator
from django.views.generic.list import ListView


@login_required
def checkout(request):
    
    def form_is_valid(post_dict):
        for field in post_dict:
            if post_dict[field] == '':
                return False

        return True


    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            cart = Cart.objects.create(user=request.user, total=0)
            request.session['cart_id'] = cart.id
            return redirect('cart')
    else:
        return redirect('checkout')

    client = get_object_or_404(ClientProfile, user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        c_form = ClientUpdateForm(data=request.POST, instance=client)
        p_form = PassportForm(data=request.POST, instance=client)
        if form_is_valid(request.POST):
            if u_form.is_valid() and c_form.is_valid() and p_form.is_valid():
                u_form.save()
                c_form.save()
                p_form.save()

                order = Order.objects.create(
                    user=request.user,
                    ref_code=refcode_generator(),
                    cart=cart,
                    total=cart.total
                )

                del request.session['cart_id']
                return redirect('cart')
        else:
            messages.error(request, 'Все поля формы обязательны для заполнения.')
            return redirect('checkout')
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = ClientUpdateForm(instance=client)
        p_form = PassportForm()


    context = {
        'u_form': u_form,
        'c_form': c_form,
        'p_form': p_form,
        'cart': cart
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def payment(request):
    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
        except:
            cart = Cart.objects.create(user=request.user, total=0)
            request.session['cart_id'] = cart.id
            return redirect('cart')
    else:
        pass

    context = {'cart': cart}
    return render(request, 'orders/payment.html', context)


def orders(request):
    pending_orders = Order.objects.filter(is_active=True)
    done_orders = Order.objects.filter(is_active=False)

    context = {
        'p_orders': pending_orders,
        'd_orders': done_orders
    }

    return render(request, 'orders/orders-edit.html', context)


def order_done(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        messages.error(request, 'Ошибка!')
        return redirect('orders-edit')

    order.is_active = False
    order.save()
    messages.success(request, f'Заказ {order.ref_code} успешно выполнен.')
    return redirect('orders-edit')