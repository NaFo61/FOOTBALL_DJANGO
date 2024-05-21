from django.urls import path
from .views import tables, table, add

app_name = "app"

urlpatterns = [
    path("tables/", tables, name="tables"),
    path("tables/<str:table>/", table, name="table"),
    path("tables/<str:table>/add/", add, name="add")
]
