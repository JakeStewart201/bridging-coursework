from django import forms
from .models import Qualification, Job, Skill, Interest, Project

class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('institution', 'course', 'start_date', 'end_date', 'text')

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('employer', 'job_title', 'start_date', 'end_date', 'text')

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('name', 'importance', 'text')

class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ('name', 'importance', 'text')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'link', 'date', 'text')
