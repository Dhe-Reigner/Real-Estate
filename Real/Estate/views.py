from django.shortcuts import render

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