from django import forms
from Eshop.models import shop

class ItemForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = ['for_user', 'item_name', 'item_desc', 'item_price', 'item_image']