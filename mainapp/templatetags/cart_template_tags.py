from django import template
from carts.models import Cart
from users.models import CLIENT


register = template.Library()

@register.filter
def cart_items_count(request):
    if request.user.profile.status == CLIENT:
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
            return len(cart.get_items())
        except:
            pass
    return 0
