# budget_app/views.py
from django.shortcuts import render
from .models import Expense, Income, BankAccount

def expense_list_view(request):
    expenses = Expense.objects.all()
    return render(request, 'budget_app/expense_list.html', {'expenses': expenses})

def income_list_view(request):
    incomes = Income.objects.all()
    return render(request, 'budget_app/expense_list.html', {'incomes': incomes})


def mask_bank_account(account_number):
    # Mask all but the last 4 digits of the account number
    masked_account = "*" * (len(account_number) - 4) + account_number[-4:]
    return masked_account

def bank_account_list_view(request):
    bank_accounts = BankAccount.objects.all()
    
    # Create a dictionary to store masked bank account numbers
    masked_bank_accounts = {}
    for account in bank_accounts:
        masked_bank_accounts[account.id] = mask_bank_account(account.account_number)
from django.shortcuts import render
from .models import Expense, Income

def expense_and_income_list_view(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()
    return render(request, 'budget_app/expense_and_income_list.html', {'expenses': expenses, 'incomes': incomes})
    