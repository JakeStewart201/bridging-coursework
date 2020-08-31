from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_page, name='cv_page'),
    path('edit_qualification/', views.edit_qualification, name='edit_qualification'),
]
