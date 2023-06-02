from django import forms
from .models import Receipt, ExpenseCategory


class ReceiptForm(forms.ModelForm):
    date = forms.DateTimeField()

    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "category", "account"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]
