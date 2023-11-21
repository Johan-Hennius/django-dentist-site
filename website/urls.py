from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="website-index-page"),
    path('contact/', views.contact, name="website-contact-page"),
]
