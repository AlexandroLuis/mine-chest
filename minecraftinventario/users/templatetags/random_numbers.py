import random
from django import template

register = template.Library()

# Para gerar o numero aleatorio para a meta
@register.simple_tag
def random_int():
    randomnumber = random.randint(15, 50)
    return randomnumber
  
# Usado para qualquer estrutura de repetição
@register.filter(name='times') 
def times(number):
    return range(number)
 