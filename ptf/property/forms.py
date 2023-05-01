
from django import forms
# from .models import Project,ProjectTeam,ProjectModule,ProjectTask
from .models import *
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =propertyDetail
        fields ='__all__'
        
    

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_buyer=True))
    
    class Meta:
        model =propertyDetail
        fields ='__all__'

class CreateProjectModuleForm(forms.ModelForm):
    class Meta:
        model = propertyDetail
        fields = '__all__'        

class CreateProjectTaskForm(forms.ModelForm):
    class Meta:
        model = propertyDetail
        fields = '__all__'        