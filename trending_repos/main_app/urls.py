from django.urls import path
from . import main_logic
app_name = 'main_app'
urlpatterns = [
    path("",main_logic.index, name="index"),
]