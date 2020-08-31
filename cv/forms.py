from django import forms
from .models import Qualification, Job

class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('institution', 'course', 'start_date', 'end_date', 'text')

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('employer', 'job_title', 'start_date', 'end_date', 'text')
