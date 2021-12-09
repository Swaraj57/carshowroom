from datetime import datetime
from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()              
    return render(request, 'contact.html')
