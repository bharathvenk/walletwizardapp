from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Income(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the bank account to a user
    account_number = models.CharField(max_length=20)  # You may adjust the max length as needed
    cvv = models.CharField(max_length=4)  # CVV can be 3 or 4 digits, adjust max length accordingly
    expiration_date = models.DateField()
    # Add other fields as needed, such as bank name, account holder's name, etc.

    def __str__(self):
        return f"Bank Account for {self.user.username}"