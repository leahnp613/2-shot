from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    date = forms.DateTimeField()

    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "category", "account"]
