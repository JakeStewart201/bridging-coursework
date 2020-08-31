from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import QualificationForm
from .models import Qualification, Job, Skill, Interest, Project

def cv_page(request):
    qualifications = Qualification.objects.order_by('start_date')
    jobs = Job.objects.order_by('start_date')
    skills = Skill.objects.order_by('importance')
    interests = Interest.objects.order_by('importance')
    projects = Project.objects.order_by('date')
    return render(request, 'cv/cv_page.html', {'qualifications': qualifications, 'jobs': jobs, 'skills': skills, 'interests': interests, 'projects': projects})

@login_required
def edit_qualification(request):
    if request.method == "POST":
        form = QualificationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cv_page')
    else:
        form = QualificationForm
    return render(request, 'cv/edit_qualification.html', {'form': form})
