from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.organizations),
    path('users/<str:org_name>', views.get_organizations_users),
    path('create_org/', views.create_organization),
    path('delete_org/<str:org>', views.delete_organization),
]