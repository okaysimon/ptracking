from django.forms import ModelForm, TextInput, Textarea, DateTimeField, DateTimeInput, FileInput, FileField
from ProjectTracking.models import Requirement


class RequirementForm(ModelForm):
    class Meta:
        model = Requirement
        fields = ['i_name', 'i_value', 'i_file']
        widgets = {
            'i_name': TextInput(attrs={'class': 'vTextField'}),
            'i_value': Textarea(attrs={'class': 'vTextField'}),
            'i_file': FileInput(attrs={'accept': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword'}),
        }
