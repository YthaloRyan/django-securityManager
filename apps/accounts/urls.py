from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('teams/', views.show_teams),
    path('teams/create', views.create_team),
    path('teams/delete', views.delete_team),
    path('teams/update', views.update_team),
]