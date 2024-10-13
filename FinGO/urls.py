from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="FinGO"),
    path('add-expensive', views.add_expense, name="add-expense")
]