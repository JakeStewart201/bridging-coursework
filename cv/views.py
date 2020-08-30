from django.shortcuts import render

from .models import Qualification

def cv_page(request):
    qualifications = Qualification.objects.order_by('start_date')
    return render(request, 'cv/cv_page.html', {'qualifications': qualifications})
