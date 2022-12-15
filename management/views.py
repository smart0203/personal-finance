import datetime
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .forms import CreateEarningForm, CreateExpenseForm, CreateDebtForm, CreateInvestmentForm
from .models import Earning, Expense, Debt, Investment, Transaction


class DashboardCreateview(LoginRequiredMixin, TemplateView):
    """
    Class Based View for Dashboard Page
    """
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        earning_data = []
        expense_data = []
        dates = []

        earning_transactions = Transaction.objects\
            .filter(category__in=["Earning", "Investment"])\
            .values('payment_date')\
            .annotate(sum=Sum('amount'))
        expense_transactions = Transaction.objects\
            .filter(category__in=["Expense", "Debt"])\
            .values('payment_date')\
            .annotate(sum=Sum('amount'))
        for i in range(today.day):
            dates.append(i + 1)
            current_date = today.replace(day=i+1)
            earning_sum = 0
            expense_sum = 0
            for earning_transaction in earning_transactions:
                if earning_transaction["payment_date"] == current_date:
                    earning_sum = earning_transaction["sum"]
                    break
            earning_data.append(earning_sum)

            for expense_transaction in expense_transactions:
                if expense_transaction["payment_date"] == current_date:
                    expense_sum = abs(expense_transaction["sum"])
                    break
            expense_data.append(expense_sum)
        
        context['earning_data'] = earning_data
        context['expense_data'] = expense_data
        context['dates'] = dates

        debt_data = []
        debt_expense_data =[]
        debts = []
        
        expenses = Expense.objects\
            .values('debt')\
            .annotate(sum=Sum('amount'))\
            .values('debt__amount','debt__interest_rate','sum')
        for item in expenses:
            debt_data.append(item["debt__amount"])
            debts.append(f"{item['debt__amount']} (rate: {item['debt__interest_rate']})")
            debt_expense_data.append(item["sum"])

        context['debt_data'] = debt_data
        context['debt_expense_data'] = debt_expense_data
        context['debts'] = debts
        
        investment_data = []
        investment_earning_data =[]
        investments = []

        earnings = Earning.objects\
            .values('investment')\
            .annotate(sum=Sum('amount'))\
            .values('investment__amount','investment__profit_rate','sum')
        for item in earnings:
            investment_data.append(item["investment__amount"])
            investments.append(f"{item['investment__amount']} (rate: {item['investment__profit_rate']})")
            investment_earning_data.append(item["sum"])

        context['investment_data'] = investment_data
        context['investment_earning_data'] = investment_earning_data
        context['investments'] = investments

        return context


class EarningCreateview(LoginRequiredMixin, CreateView):
    """
    Class Based View for Earning List/Create Page
    """
    model = Earning
    form_class = CreateEarningForm
    template_name = "earning/create.html"
    success_url = reverse_lazy('management:earnings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['earnings'] = Earning.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if self.object.category == "Investment":
            self.object.period = "One Time"
        self.object.save()

        # Create a new transaction record
        try:
            Transaction.objects.create(
                user=self.request.user,
                category="Investment" if self.object.category == "Investment" else "Earning",
                amount=self.object.amount,
                payment_date=self.object.payment_start_date,
                notes=self.object.notes
            )
        except:
            pass
        return super().form_valid(form)


class EarningUpdateview(LoginRequiredMixin, UpdateView):
    """
    Class Based View for Earning Edit Page
    """
    model = Earning
    form_class = CreateEarningForm
    template_name = "update.html"
    success_url = reverse_lazy('management:earnings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Earning"
        return context


class EarningDeleteview(LoginRequiredMixin, DeleteView):
    """
    Class Based View for Earning Delete Page
    """
    model = Earning
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('management:earnings')


class ExpenseCreateview(CreateView):
    """
    Class Based View for Expense List/Create Page
    """
    model = Expense
    form_class = CreateExpenseForm
    template_name = "expense/create.html"
    success_url = reverse_lazy('management:expenses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if self.object.category == "Debt":
            self.object.period = "One Time"
        self.object.save()

        # Create a new transaction record
        try:
            Transaction.objects.create(
                user=self.request.user,
                category="Debt" if self.object.category == "Debt" else "Expense",
                amount=-self.object.amount,
                payment_date=self.object.payment_start_date,
                notes=self.object.notes
            )
        except:
            pass

        return super().form_valid(form)


class ExpenseUpdateview(LoginRequiredMixin, UpdateView):
    """
    Class Based View for Expense Edit Page
    """
    model = Expense
    form_class = CreateExpenseForm
    template_name = "update.html"
    success_url = reverse_lazy('management:expenses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Expense"
        return context


class ExpenseDeleteview(LoginRequiredMixin, DeleteView):
    """
    Class Based View for Expense Delete Page
    """
    model = Expense
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('management:expenses')


class DebtCreateview(CreateView):
    """
    Class Based View for Debt List/Create Page
    """
    model = Debt
    form_class = CreateDebtForm
    template_name = "debt/create.html"
    success_url = reverse_lazy('management:debt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debts'] = Debt.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DebtUpdateview(LoginRequiredMixin, UpdateView):
    """
    Class Based View for Debt Edit Page
    """
    model = Debt
    form_class = CreateDebtForm
    template_name = "update.html"
    success_url = reverse_lazy('management:debt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Debt"
        return context


class DebtDeleteview(LoginRequiredMixin, DeleteView):
    """
    Class Based View for Debt Delete Page
    """
    model = Debt
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('management:debt')


class InvestmentCreateview(CreateView):
    """
    Class Based View for Investment List/Create Page
    """
    model = Investment
    form_class = CreateInvestmentForm
    template_name = "investment/create.html"
    success_url = reverse_lazy('management:investment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investments'] = Investment.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class InvestmentUpdateview(LoginRequiredMixin, UpdateView):
    """
    Class Based View for Investment Edit Page
    """
    model = Investment
    form_class = CreateInvestmentForm
    template_name = "update.html"
    success_url = reverse_lazy('management:investment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Investment"
        return context


class InvestmentDeleteview(LoginRequiredMixin, DeleteView):
    """
    Class Based View for Investment Delete Page
    """
    model = Investment
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('management:investment')