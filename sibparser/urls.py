from django.urls import include, path
from . import views

app_name = "sensors"
urlpatterns = [path('', views.IndexView.as_view(), name="index")]