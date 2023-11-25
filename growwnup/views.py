from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def workshop(request):
    return render(request, 'pages/workshop.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def engCommunication(request):
    return render(request, 'pages/English-Communication.html')

def display(request):
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    wp = request.POST.get('wp')
    ans = request.POST.get('ans')
    submitbutton = request.POST.get('submit')

    context= {'fullname': fullname, 'email':email,
              'wp': wp, 'ans': ans,
              'submitbutton': submitbutton}
    print(fullname)
    
    return render(request, 'form/display.html', context)