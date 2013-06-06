from itertools import izip
from django import template

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
    
def hello(text):
    """Removes all values of arg from the given string"""
    return "Hello, " + text
    
#@register.filter
#def classes(field):
#    """    Returns CSS classes of a field    """
#    return field.field.widget.attrs.get('class', None)    
    
#@register.filter('klass')
#def klass(ob):
#    return "Diego"   
