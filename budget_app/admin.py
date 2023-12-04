# budget_app/admin.py
from django.contrib import admin
from .models import Category, Expense, Income, BankAccount

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(BankAccount)