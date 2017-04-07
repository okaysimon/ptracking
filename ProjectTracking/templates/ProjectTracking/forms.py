from django.forms import ModelForm
from ProjectTracking.models import Requirement


class RequirementForm(ModelForm):
    class Meta:
        model = Requirement
        fields = ['r_info_name', 'r_info_value', 'r_info_submit_employee']
