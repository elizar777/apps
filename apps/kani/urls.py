from django.urls import path
from apps.kani.views import index

urlpatterns = [
    path('', index, name='index')
]