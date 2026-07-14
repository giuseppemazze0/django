from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),

    path("magic_login/", views.magic_link_login, name="magic_login"),
    path("magic_login_confirm/<uidb64>/<token>/", views.magic_login_confirm, name="magic_login_confirm"),
]