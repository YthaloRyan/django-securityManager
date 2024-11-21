from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.organizations),
    path('users/<str:org_name>', views.get_organizations_users),
    path('create_org/', views.create_organization),
    path('delete_org/<str:org>', views.delete_organization),
    path('add_users/<str:org>', views.add_users_by_org),
    path('remove_user/<str:org>/<str:username>', views.delete_user_from_org),
]