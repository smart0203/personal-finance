from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Earning, Expense, Debt, Investment


class CreateEarningForm(forms.ModelForm):

    class Meta:
        model = Earning
        fields = ["category", "investment", "period", "amount", "payment_start_date", "payment_end_date"]

    def __init__(self, *args, **kwargs):
        super(CreateEarningForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    

class CreateExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ["category", "debt", "period", "amount", "payment_start_date", "payment_end_date"]

    def __init__(self, *args, **kwargs):
        super(CreateExpenseForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class CreateDebtForm(forms.ModelForm):

    class Meta:
        model = Debt
        fields = ["category", "interest_rate", "amount", "start_date", "end_date"]

    def __init__(self, *args, **kwargs):
        super(CreateDebtForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class CreateInvestmentForm(forms.ModelForm):

    class Meta:
        model = Investment
        fields = ["category", "profit_rate", "amount", "start_date", "end_date"]

    def __init__(self, *args, **kwargs):
        super(CreateInvestmentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))