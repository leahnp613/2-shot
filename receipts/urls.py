from django.urls import path
from receipts.views import receipt_list, create_receipt


# app_name = "receipts"
urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
