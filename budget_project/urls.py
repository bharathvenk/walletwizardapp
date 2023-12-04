from django.contrib import admin
from django.urls import path
from budget_app.views import expense_and_income_list_view  # Import the combined view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', expense_and_income_list_view, name='expense_and_income_list'),  # Root URL for combined list
]
