from django import forms
from .models import Qualification

class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('institution', 'course', 'start_date', 'end_date', 'text')
