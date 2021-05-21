import random
from django import template

register = template.Library()

@register.simple_tag
def random_int():
    return random.randint(150, 500)
    
@register.simple_tag    
def sum():
    sum = 0
    return sum