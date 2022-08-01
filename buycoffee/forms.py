from django.forms import ModelForm
from .models import Order


class order_form(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

