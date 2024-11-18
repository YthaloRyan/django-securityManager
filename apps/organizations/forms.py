from django import forms


from .models import Organization

class OrgCreationForm(forms.ModelForm):
    class Meta:
        model = Organization
        
        fields = ['name', 'description', 'org_admin']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple,  # Para exibir opções como checkboxes
        }
        
    def __init__(self, *args, **kwargs):
        super(OrgCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control form-control-lg'