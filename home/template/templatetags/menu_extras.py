from django import template

register = template.Library()

@register.filter
def availability_status(is_available):
    """
    Returns 'Coming Soon' if the menu item is unavailable.
    
    """
    return "Available" if is_available else "Coming Soom"