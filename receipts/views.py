from django.shortcuts import render
from .models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def receipt_list(request):
    receipt_list = Receipt.objects.filter(purchaser = request.user.id)
    context = {"receipt_list": receipt_list}

    return render(request, "list.html", context)
