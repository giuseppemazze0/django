from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="desenvolvedor"),
    path('tfcs/', views.tfcs_view, name="tfcs"),
    path('faculdade/', views.faculdade_view, name="faculdade"),
]