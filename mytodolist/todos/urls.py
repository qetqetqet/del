# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Assuming you have a view named 'index' in 'todos/views.py'
    # ... other url patterns for your todos app ...
]
