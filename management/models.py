from django.db import models
from django.contrib.auth.models import User


class Debt(models.Model):
    """
    Represent Debt per User
    """
    DEBT_CATEGORY = (
        ("Short Term", "Short Term"),
        ("Long Term", "Long Term")
    )

    user = models.ForeignKey(User, related_name="debts", on_delete = models.CASCADE)
    category = models.CharField(
        max_length = 100,
        choices = DEBT_CATEGORY,
        default = "Short Term"
    )
    # interest_rate is decimal field like 5.00%, and its monthly rate by assuming
    interest_rate = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['amount']

    def __str__(self):
        return str(self.amount) + " (rate: " + str(self.interest_rate) + ")"
    

class Expense(models.Model):
    """
    Represent Expense per User
    """
    EXPENSE_PERIOD = (
        ("One Time", "One Time"),
        ("Weekly", "Weekly"),
        ("Bi-Weekly", "Bi-Weekly"),
        ("Monthly", "Monthly"),
        ("Annually", "Annually")
    )
    EXPENSE_CATEGORY = (
        ("Debt", "Debt"),
        ("Food", "Food"),
        ("Electricity", "Electricity"),
        ("Car", "Car"),
        ("Petrol", "Petrol"),
        ("Property", "Property"),
        ("Other", "Other")
    )

    user = models.ForeignKey(User, related_name="expenses", on_delete = models.CASCADE)
    category = models.CharField(
        max_length = 100,
        choices = EXPENSE_CATEGORY,
        default = "Other"
    )
    period = models.CharField(
        max_length = 100,
        choices = EXPENSE_PERIOD,
        default = "One Time"
    )
    debt = models.ForeignKey(Debt, related_name="debts", on_delete = models.CASCADE, default=0)
    amount = models.PositiveIntegerField(default=0)
    payment_start_date = models.DateField()
    payment_end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class Investment(models.Model):
    """
    Represent Investment Model per User
    """
    INVESTMENT_CATEGORY = (
        ("Stock", "Stock"),
        ("Forex", "Forex"),
        ("Real Estate", "Real Estate"),
        ("Cryptocurrency", "Cryptocurrency"),
        ("Other", "Other")
    )
    user = models.ForeignKey(User, related_name="investments", on_delete = models.CASCADE)
    category = models.CharField(
        max_length = 100,
        choices = INVESTMENT_CATEGORY,
        default = "Other"
    )
    # profit_rate is decimal field like 5.00%, and its monthly rate by assuming
    profit_rate = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount) + " (rate: " + str(self.profit_rate) + ")"


class Earning(models.Model):
    """
    Represent Earning per User
    """
    EARNING_PERIOD = (
        ("One Time", "One Time"),
        ("Weekly", "Weekly"),
        ("Bi-Weekly", "Bi-Weekly"),
        ("Monthly", "Monthly"),
        ("Annually", "Annually")
    )
    EARNING_CATEGORY = (
        ("Normal", "Normal"),
        ("Investment", "Investment")
    )

    user = models.ForeignKey(User, related_name="earnings", on_delete = models.CASCADE)
    category = models.CharField(
        max_length = 100,
        choices = EARNING_CATEGORY,
        default = "Normal"
    )
    period = models.CharField(
        max_length = 100,
        choices = EARNING_PERIOD,
        default = "One Time"
    )
    investment = models.ForeignKey(Investment, related_name="investments", on_delete = models.CASCADE, default=0)
    amount = models.PositiveIntegerField(default=0)
    payment_start_date = models.DateField()
    payment_end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    """
    Represent Investment Model per User
    """
    TRANSACTION_CATEGORY = (
        ("Earning", "Earning"),
        ("Expense", "Expense"),
        ("Debt", "Debt"),
        ("Investment", "Investment")
    )
    user = models.ForeignKey(User, related_name="transactions", on_delete = models.CASCADE)
    category = models.CharField(
        max_length = 100,
        choices = TRANSACTION_CATEGORY,
        default = "Earning"
    )
    amount = models.IntegerField(default=0)
    payment_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)