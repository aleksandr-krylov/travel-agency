import string
import random
from .models import Order

def refcode_generator(length=10, chars=string.ascii_uppercase + string.digits):
    ref_code = ''.join(random.choice(chars) for _ in range(length))
    """
    try:
        order  = Order.objects.get(ref_code=ref_code)
        refcode_generator()

    except Order.DoesNotExist:"""
    return ref_code

