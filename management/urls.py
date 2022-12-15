from django.urls import path

from .views import EarningCreateview, EarningUpdateview, EarningDeleteview,\
    ExpenseCreateview, ExpenseUpdateview, ExpenseDeleteview, DebtCreateview,\
    DebtUpdateview, DebtDeleteview, InvestmentCreateview, InvestmentUpdateview,\
    InvestmentDeleteview, DashboardCreateview

app_name = 'management'

urlpatterns = [
    path('dashboard', DashboardCreateview.as_view(), name='dashboard'),

    path('earning', EarningCreateview.as_view(), name="earnings"),
    path('earning/edit/<int:pk>', EarningUpdateview.as_view(), name="earnings_edit"),
    path('earning/delete/<int:pk>', EarningDeleteview.as_view(), name="earnings_delete"),

    path('expense', ExpenseCreateview.as_view(), name="expenses"),
    path('expense/edit/<int:pk>', ExpenseUpdateview.as_view(), name="expenses_edit"),
    path('expense/delete/<int:pk>', ExpenseDeleteview.as_view(), name="expenses_delete"),

    path('debt_management', DebtCreateview.as_view(), name="debt"),
    path('debt/edit/<int:pk>', DebtUpdateview.as_view(), name="debt_edit"),
    path('debt/delete/<int:pk>', DebtDeleteview.as_view(), name="debt_delete"),

    path('investment', InvestmentCreateview.as_view(), name="investment"),
    path('investment/edit/<int:pk>', InvestmentUpdateview.as_view(), name="investment_edit"),
    path('investment/delete/<int:pk>', InvestmentDeleteview.as_view(), name="investment_delete"),
]