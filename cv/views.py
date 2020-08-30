from django.shortcuts import render

from .models import Qualification, Job, Skill, Interest, Project

def cv_page(request):
    qualifications = Qualification.objects.order_by('start_date')
    jobs = Job.objects.order_by('start_date')
    skills = Skill.objects.order_by('importance')
    interests = Interest.objects.order_by('importance')
    projects = Project.objects.order_by('date')
    return render(request, 'cv/cv_page.html', {'qualifications': qualifications, 'jobs': jobs, 'skills': skills, 'interests': interests, 'projects': projects})
