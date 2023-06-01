from django.urls import path
from receipts.views import receipt_list

app_name = "receipts"
urlpatterns = [
    path("", receipt_list, name="home"),
]
