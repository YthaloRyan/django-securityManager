from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

from .models import Organization


from .forms import OrgCreationForm

# Create your views here.
@login_required
def organizations(request):
    organizations = Organization.objects.all()
    
    infos = {
        'organizations': organizations,
    }
    
    return render(request, 'organizations/org.html', infos)


@login_required
def get_organizations_users(request, org):
    auth = False
    actual_user = get_object_or_404(User, username=request.user)
    actual_user_organizations = actual_user.organizations.all()
    
    roles = ["Admin", "OrgAdmin"]
    auth = any(org.name in roles for org in actual_user_organizations)
    
    
    organization = get_object_or_404(Organization, name=org)
    
    users = organization.users.all()
    
    infos = {
        'users': users,
        'org': org,
        'auth': auth,
    }
    return render(request, 'organizations/list_users.html', infos)


@login_required
def create_organization(request):
    form = OrgCreationForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            return render(request, 'organizations/create_user.html', {'form': form})
        
        else:
            return render(request, 'organizations/create_user.html', {'form': form}, status=400)
        
        
        
    
    return render(request, 'organizations/create_user.html', {'form': form})