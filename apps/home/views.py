from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User



# Create your views here.
@login_required
def home(request):
    user = get_object_or_404(User, username=request.user)
    
    organizations = user.organizations.all()
    
    infos = {
        'username': user,
        'organizations': organizations,
    }
    
    
    return render(request, 'home/home.html', infos)