from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    current_user = request.user
    
    infos = {
        'username': current_user,
    }
    print(current_user)
    
    return render(request, 'home/home.html', {'infos': infos})