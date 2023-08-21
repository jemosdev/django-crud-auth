from django.forms import ModelForm
from .models import Task

#form can sent to the frontend
class TaskForm(ModelForm):
    class Meta:
        model= Task     #based on model Task
        fields= ['title','description','important']