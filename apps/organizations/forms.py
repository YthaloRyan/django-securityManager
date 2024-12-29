from django import forms


from .models import Organization
from django.contrib.auth.models import Group, User


from django.db.models import Q

class OrgCreationForm(forms.ModelForm):
    class Meta:
        model = Organization
        
        fields = ['name', 'description', 'org_admin']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
        
    def __init__(self, *args, **kwargs):
        super(OrgCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control form-control-lg'
            
            
class AddUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True
    )
    
    
    class Meta:
        model = Organization
        
        fields = ['users']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
        
    def __init__(self, *args, **kwargs):
        organization = kwargs.pop('organization', None)
        super(AddUserForm, self).__init__(*args, **kwargs)
        
        if organization:
            organization_model = Organization.objects.get(name=organization)
    
            users = User.objects.exclude(
                Q(organizations=organization_model) | Q(org_admin=organization_model)
            )
            
            self.fields['users'].queryset = users
            
            
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control form-control-lg'
            
            
class EditUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=True
    )
    
    
    class Meta:
        model = User
        fields = ['username', 'groups']
        
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
        
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control form-control-lg'
        
