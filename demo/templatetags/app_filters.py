from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def day_differnce(value, end_day):
    from datetime import datetime
    date_format = "%m/%d/%Y"
    a = datetime.strptime(value, date_format)
    b = datetime.strptime(end_day, date_format)
    differnce = b - a
    return differnce.days