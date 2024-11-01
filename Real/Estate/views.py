from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']


            # send an email
            send_mail(
              'message from ' + name, # subject
                message, # message
                email, # from email
                ['ngashtabbs@gmail.com','martinkagema01@gmail.com'], # To Email
            )

            return render(request, 'contact.html', {'name': name})
    else:    
      return render(request, 'contact.html')

def property_list(request):
    return render(request, 'property_list.html')

def property_agent(request):
    return render(request, 'property_agent.html')

def property_type(request):
    return render(request, 'property_type.html')

def testimonial(request):
    return render(request, 'testimonial.html')