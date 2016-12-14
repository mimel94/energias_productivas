from django import template

register = template.library()

@register.filter(name=’cortar’)
def cortar(value,arg):
    return value.replace(arg,'')
@register.filter
def minusculas(valor):
    return valor.lower()
