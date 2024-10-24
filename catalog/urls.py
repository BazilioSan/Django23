from config.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>/", product_details, name="product_details"),
]