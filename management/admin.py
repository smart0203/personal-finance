from django.contrib import admin

from .models import Earning, Expense, Debt, Investment


class EarningAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "period", "amount", "payment_start_date", "payment_end_date")


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "period", "amount", "payment_start_date", "payment_end_date")


class DebtAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "interest_rate", "amount", "start_date", "end_date")


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "profit_rate", "amount", "start_date", "end_date")


admin.site.register(Earning, EarningAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Debt, DebtAdmin)
admin.site.register(Investment, InvestmentAdmin)
