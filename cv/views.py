from django.shortcuts import render
from django.http import HttpResponse

def cv_page(request):
    return HttpResponse('\n<html><title>Jake\'s CV</title></html>\n')
