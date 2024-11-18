from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.organizations),
    path('users/<str:org>', views.get_organizations_users),
    path('create_org/', views.create_organization),
    # path('add_user/', views.home),
]