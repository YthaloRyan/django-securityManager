from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

from .models import Organization


from django.db.models import Q

from .forms import OrgCreationForm, AddUserForm


#UTILS

    


#VIEWS
# Create your views here.
@login_required
def organizations(request):
    organizations = Organization.objects.all()
    
    for org in organizations:
        print(org)
        print('='*20)
    
    infos = {
        'organizations': organizations,
    }
    
    return render(request, 'organizations/org.html', infos)


@login_required
def get_organizations_users(request, org_name):
    actual_user = get_object_or_404(User, username=request.user)
    actual_user_organizations = actual_user.groups.all()
    
    
    roles = ["Admin", "OrgAdmin"]
    auth = any(org.name in roles for org in actual_user_organizations)
    
    
    organization = get_object_or_404(Organization, name=org_name)
    
    
    users = organization.users.all()
    
    org_admins = organization.org_admin.all()
    
    infos = {
        'users': users,
        'org': org_name,
        'org_admins': org_admins,
        'auth': auth,
    }
    
    return render(request, 'organizations/list_users.html', infos)


@login_required
def create_organization(request):
    form = OrgCreationForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            return render(request, 'organizations/create_org.html', {'form': form})
        
        else:
            return render(request, 'organizations/create_org.html', {'form': form}, status=400)
        
        
    return render(request, 'organizations/create_org.html', {'form': form})


@login_required
def delete_organization(request, org):
    if request.method == "DELETE":
        try:
            print(org)
            organization = get_object_or_404(Organization, name=org)
    
            organization.delete()
            return JsonResponse({"message": "Item deletado com sucesso."})
        except Organization.DoesNotExist:
            return JsonResponse({"error": "Item não encontrado."}, status=404)
    return HttpResponseBadRequest("Método não permitido")


@login_required
def add_users_by_org(request, org):
    organization = get_object_or_404(Organization, name=org)
    
    form = AddUserForm(request.POST,organization=org,instance=organization or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            return redirect('/organizations')
        
        else:
            return render(request, 'organizations/add_user.html', {'form': form}, status=400)
    
    
    infos = {
        'org': org,
        'form': form,
    }
    
    return render(request, 'organizations/add_user.html', infos)
    