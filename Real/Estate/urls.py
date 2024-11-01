from django.urls import path 
from .views import home, about, contact, property_list, property_agent, property_type, testimonial

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('property_list/', property_list, name='property_list'),
    path('property_agent/', property_agent, name='property_agent'),
    path('property_type/', property_type, name='property_type'),
    path('testimonial/', testimonial, name='testimonial'),
   
]