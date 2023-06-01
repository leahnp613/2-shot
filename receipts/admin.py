from django.contrib import admin

from receipts.models import ExpenseCategory, Receipt, Account


# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategoryAdminm(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "total",
        "tax",
        "date",
        "purchaser",
        "category",
        "account",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "owner",
    )
