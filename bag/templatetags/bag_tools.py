from django import template

register = template.Library()
# register function as a template filter


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
