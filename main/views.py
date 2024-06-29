from django.shortcuts import render
from .models import Contact, Service
# Create your views here.
from django.contrib import messages
def index(request):
    services = Service.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_user = Contact.objects.create(name = name,email = email , message = message)
        contact_user.save()
        messages.success(request,'Thank you for the info, contact you soon')
    return render(request,'main/index.html',{'services':services})


def component(request):
    return render(request,'main/components.html')