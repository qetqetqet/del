# mytodolist/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),  # This line should refer to the URLs in your 'todos' app
    # ... other paths ...
]

