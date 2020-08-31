from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_page, name='cv_page'),
    path('edit_qualification/', views.edit_qualification, name='edit_qualification'),
    path('edit_job/', views.edit_job, name='edit_job'),
    path('edit_skill/', views.edit_skill, name='edit_skill'),
]
