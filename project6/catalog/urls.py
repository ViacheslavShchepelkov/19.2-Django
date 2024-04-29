from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', home, name='home')
]

